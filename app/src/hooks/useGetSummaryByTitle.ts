import useAxiosInstance from '@/lib/axios-instance';
import { useMutation } from '@tanstack/react-query';
import { useNavigate } from 'react-router-dom';

export interface TitleSchema
{
    title: string,
}

const useGetSummaryByTitle = () => {
  const navigate = useNavigate();
  const axiosInstance = useAxiosInstance();


  const getSummaryByTitle = async (values: TitleSchema) => {
    const response = await axiosInstance.post('/summary', values);
    return response?.data;
  };

  const { mutate, isPending, isSuccess } = useMutation({
    mutationFn : getSummaryByTitle,
    onSuccess : (response,param) => {
      navigate('/title-page-summary', {
        state :  {
          summary : response?.data?.summary?.summary_text,
          title: param.title
        }
      })
    }
  });

  const onSubmit = (values: TitleSchema) => {
     console.log(values);
    
      mutate(values);
  };

  return { onSubmit, isPending, isSuccess };
};

export default useGetSummaryByTitle;