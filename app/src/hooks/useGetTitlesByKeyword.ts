import useAxiosInstance from "@/lib/axios-instance";
import { zodResolver } from "@hookform/resolvers/zod";
import { useMutation } from "@tanstack/react-query";
import { useForm } from "react-hook-form";
import { useNavigate } from "react-router-dom";
import { z } from "zod";

export interface TitleSchema {
  query: string;
}

const useGetTitlesByKeyword = () => {
  const navigate = useNavigate();
  const inputSchema = z.object({
    query: z.string({ required_error: "Keyword is required" }).min(1),
  });

  const form = useForm<z.infer<typeof inputSchema>>({
    resolver: zodResolver(inputSchema),
  });

  const axiosInstance = useAxiosInstance();

  const getTitlesByKeyword = async (values: z.infer<typeof inputSchema>) => {
    const response = await axiosInstance.post("/search", values);
    return response?.data;
  };

  const { mutate, isPending, isSuccess} = useMutation({
    mutationFn: getTitlesByKeyword,
    onSuccess : async (response) => {
      navigate('/', {
        state :  {
          titles : await response,
        }
      })
    }
  });

  const SubmitHandler = (values: z.infer<typeof inputSchema>) => {
    mutate(values);
  };

  return { form, SubmitHandler, isPending, isSuccess };
};

export default useGetTitlesByKeyword;
