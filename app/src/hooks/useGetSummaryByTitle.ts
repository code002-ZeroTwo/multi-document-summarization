import useAxiosInstance from '@/lib/axios-instance';
import { useMutation } from '@tanstack/react-query';

export interface TitleSchema
{
    title: string,
}

const useGetSummaryByTitle = () => {

  const axiosInstance = useAxiosInstance();


  const getSummaryByTitle = async (values: TitleSchema) => {
    const response = await axiosInstance.post('/summary', {
        data: values
    });
    return response?.data;
  };

  const { mutate, isPending, isSuccess } = useMutation({
    mutationFn : getSummaryByTitle
  });

  const onSubmit = (values: TitleSchema) => {
    console.log(values);
    
      mutate(values);
  };

  return { onSubmit, isPending, isSuccess };
};

export default useGetSummaryByTitle;