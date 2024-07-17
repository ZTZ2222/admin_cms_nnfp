import React from "react";

export default function PublicLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <>
      <div className="p-5">Public Layout</div>
      {children}
    </>
  );
}
