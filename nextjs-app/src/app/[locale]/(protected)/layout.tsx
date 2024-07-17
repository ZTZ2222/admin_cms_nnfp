import { redirect } from "@/lib/i18n";

export default async function ProtectedLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  const session = true; // TODO: implement session check
  if (!session) {
    redirect("/login");
  }

  return <>{children}</>;
}
