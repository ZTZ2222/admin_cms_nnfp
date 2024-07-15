import GoogleProvider from "next-auth/providers/google";
import CredentialsProvider from "next-auth/providers/credentials";
import type { NextAuthOptions } from "next-auth";

const { GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET } = process.env;

export const authOptions: NextAuthOptions = {
  providers: [
    CredentialsProvider({
      name: "Credentials",
      credentials: {
        email: { label: "Email", type: "text" },
        password: { label: "Password", type: "password" },
      },
      async authorize(credentials) {
        try {
          const { email, password } = credentials as {
            email: string;
            password: string;
          };
          return null;
        } catch (error) {
          return null;
        }

        // TODO: Implement fetch to check credentials
      },
    }),
    GoogleProvider({
      clientId: String(GOOGLE_CLIENT_ID),
      clientSecret: String(GOOGLE_CLIENT_SECRET),
    }),
  ],
  session: {
    strategy: "jwt",
  },
  secret: process.env.NEXTAUTH_SECRET,
  callbacks: {
    async jwt({ token, user }) {
      return { ...token, ...user };
    },
    async session({ session, token }) {
      session.user = token as any;
      return session; // The return type will match the one returned in `useSession()`
    },
    async signIn({ account, profile }) {
      // https://next-auth.js.org/providers/google
      if (account?.provider === "google" && !profile?.email) {
        return false;
      }

      try {
        return true;
      } catch (error) {
        console.error(error);

        return false;
      }
    },
  },
};
