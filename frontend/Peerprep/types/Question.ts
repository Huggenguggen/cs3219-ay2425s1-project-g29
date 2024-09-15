export type Question = {
  id?: number;
  title: string;
  description: string;
  category: string;
  complexity: "easy" | "medium" | "hard";
};
