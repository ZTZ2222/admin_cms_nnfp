import { Button } from "@/components/ui/button";
import Link from "next/link";

export default function Home() {
  return (
    <main className="grid min-h-screen w-full place-content-center">
      <div>User ID: Undefined</div>
      <Button asChild variant="link" size="default">
        <Link href="/auth/login">Go to login page</Link>
      </Button>
    </main>
  );
}
