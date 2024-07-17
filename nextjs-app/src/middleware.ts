import { NextRequest } from "next/server";
import createMiddleware from "next-intl/middleware";
import { AllLocales, AppConfig } from "./lib/i18n";

// Define public pages and paths that don't require authentication
const publicPages = ["/", "/login"];

async function isAuthenticated(req: NextRequest): Promise<boolean> {
  const token = true;
  return !!token;
}

// Internationalization middleware
const intlMiddleware = createMiddleware({
  locales: AllLocales,
  localePrefix: AppConfig.localePrefix,
  defaultLocale: AppConfig.defaultLocale,
});

const authMiddleware = async (req: NextRequest) => {
  const isPublicPage = publicPages.some((page) =>
    req.nextUrl.pathname.match(page),
  );
  if (isPublicPage) {
    return intlMiddleware(req);
  }

  const isAuthenticatedUser = await isAuthenticated(req);
  if (isAuthenticatedUser) {
    return intlMiddleware(req);
  }

  // Redirect to login page if not authenticated
  return {
    status: 302,
    redirect: { destination: "/login", permanent: false },
  };
};

// Middleware function to determine whether to apply authentication or not
export default async function middleware(req: NextRequest) {
  // Apply authentication logic
  return await authMiddleware(req);
}

export const config = {
  matcher: ["/((?!api|_next|.*\\..*).*)"],
};
