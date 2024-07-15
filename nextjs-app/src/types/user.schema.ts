import { z } from "zod";

export const BaseUserSchema = z.object({
  email: z.string().email(),
  name: z.string().optional(),
});

export const PasswordUserSchema = BaseUserSchema.extend({
  password: z.string().min(8),
});

export const SocialUserSchema = BaseUserSchema.extend({
  provider: z.enum(["google", "facebook"]),
  providerId: z.string(),
});

export const ReadUserSchema = BaseUserSchema.extend({
  id: z.number(),
  is_active: z.boolean(),
  is_superuser: z.boolean(),
});

export type zPasswordUser = z.infer<typeof PasswordUserSchema>;
export type zSocialUser = z.infer<typeof SocialUserSchema>;
export type zReadUser = z.infer<typeof ReadUserSchema>;
