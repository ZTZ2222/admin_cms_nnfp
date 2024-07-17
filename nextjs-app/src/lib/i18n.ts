import { notFound } from "next/navigation";
import { getRequestConfig } from "next-intl/server";
import { LocalePrefix } from "next-intl/routing";
import { createSharedPathnamesNavigation } from "next-intl/navigation";

const localePrefix: LocalePrefix = "as-needed";

export const AppConfig = {
  name: "Dashboard",
  locales: [
    {
      id: "ru",
      name: "Русский",
    },
    {
      id: "en",
      name: "English",
    },
    {
      id: "ky",
      name: "Кыргызча",
    },
  ],
  defaultLocale: "ru",
  localePrefix,
};

export const AllLocales = AppConfig.locales.map((locale) => locale.id);

export default getRequestConfig(async ({ locale }) => {
  // Validate that the incoming `locale` parameter is valid
  if (!AllLocales.includes(locale as any)) notFound();

  return {
    messages: (await import(`../locales/${locale}.json`)).default,
  };
});

export const getI18nPath = (url: string, locale: string) => {
  if (locale === AppConfig.defaultLocale) {
    return url;
  }

  return `/${locale}${url}`;
};

export const { Link, usePathname, useRouter, redirect } =
  createSharedPathnamesNavigation({
    locales: AllLocales,
    localePrefix: AppConfig.localePrefix,
  });
