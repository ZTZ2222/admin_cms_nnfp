import { Button } from "@/components/ui/button";
import Link from "next/link";

export default function Home() {
  return (
    <main className="grid min-h-screen w-full place-content-center">
      <div className="p-5">Home Page</div>
      <Button asChild variant="link" size="default">
        <Link href="/dashboard">Go to Dashboard</Link>
      </Button>
      <Button asChild variant="link" size="default">
        <Link href="/login">Go to Login</Link>
      </Button>
    </main>
  );
}
