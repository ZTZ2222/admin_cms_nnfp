import { NextFetchEvent, NextRequest } from "next/server";
import { NextRequestWithAuth, withAuth } from "next-auth/middleware";
import createMiddleware from "next-intl/middleware";
import { AllLocales, AppConfig } from "./lib/i18n";
import { NextMiddlewareResult } from "next/dist/server/web/types";

const publicPages = [
  "/",
  "/login",
  "/user-posts",
  "/privacy-policy",
  "/cookies-consent",
  "/terms-of-use",
];

export const intlMiddleware = createMiddleware({
  locales: AllLocales,
  localePrefix: AppConfig.localePrefix,
  defaultLocale: AppConfig.defaultLocale,
});

type AuthMiddleware = (
  request: NextRequestWithAuth | NextRequest,
  event?: NextFetchEvent,
) => Promise<NextMiddlewareResult>;

const authMiddleware = withAuth((req) => intlMiddleware(req), {
  callbacks: {
    authorized: ({ token }) => !!token,
  },
  pages: { signIn: "/login" },
}) as AuthMiddleware;

export default function middleware(req: NextRequest) {
  const publicPathRegex = new RegExp(
    `^(/(${AllLocales.join("|")}))?(${publicPages.join("|")})?/?$`,
    "i",
  );

  return publicPathRegex.test(req.nextUrl.pathname)
    ? intlMiddleware(req)
    : authMiddleware(req);
}

export const config = {
  matcher: ["/((?!api|_next|.*\\..*).*)"],
};
