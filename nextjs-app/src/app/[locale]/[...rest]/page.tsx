import Link from "next/link";

export default async function Error404() {
  return (
    <div className="flex min-h-screen flex-col">
      <main className="grow">
        <div className="container space-y-8 py-24 text-center">
          <p className="text-6xl">404</p>

          <div>
            <Link href="/">Link</Link>
          </div>
        </div>
      </main>
    </div>
  );
}
