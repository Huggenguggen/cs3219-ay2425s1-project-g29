import { h } from "vue";
import type { ColumnDef } from "@tanstack/vue-table";
import type { Question } from "~/types/Question";
import QuestionTableDropDown from "./QuestionTableDropDown.vue";

export const columns: ColumnDef<Question>[] = [
  { accessorKey: "id", header: "Id" },
  { accessorKey: "title", header: "Title" },
  { accessorKey: "description", header: "Description" },
  { accessorKey: "category", header: "Category" },
  { accessorKey: "difficulty", header: "Difficulty" },
  {
    id: "actions",
    enableHiding: false,
    cell: ({ row }) => {
      const question = row.original;

      return h(
        "div",
        { class: "relative" },
        h(QuestionTableDropDown, {
          question,
        })
      );
    },
  },
];
