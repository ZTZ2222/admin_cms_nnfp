export default async function WithNavbarLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <div className="flex w-full">
      {/* <Navbar> */}
      {children}
      {/* </Navbar> */}
    </div>
  );
}
