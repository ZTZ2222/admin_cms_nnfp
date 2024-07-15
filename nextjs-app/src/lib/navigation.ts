import { createSharedPathnamesNavigation } from "next-intl/navigation";
import { AllLocales, AppConfig } from "./i18n";

export const { usePathname, useRouter, redirect } =
  createSharedPathnamesNavigation({
    locales: AllLocales,
    localePrefix: AppConfig.localePrefix,
  });
