import { z } from "zod";

export const TokenSchema = z.object({
  access_token: z.string(),
  token_type: z.string(),
});

export const TokenPayloadSchema = z
  .object({
    sub: z.string(),
    exp: z.number(),
    iat: z.number(),
    iss: z.string(),
    username: z.string(),
    is_active: z.boolean(),
    is_superuser: z.boolean(),
  })
  .nullable();

export type zToken = z.infer<typeof TokenSchema>;
export type zTokenPayload = z.infer<typeof TokenPayloadSchema>;
