import { z } from "zod";

export const TokenPayloadSchema = z
  .object({
    sub: z.string(),
    exp: z.number(),
    iat: z.number(),
    iss: z.string(),
    username: z.string(),
    is_active: z.boolean(),
    is_admin: z.boolean(),
  })
  .nullable();

export type zTokenPayload = z.infer<typeof TokenPayloadSchema>;
