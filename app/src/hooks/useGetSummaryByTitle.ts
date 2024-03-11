import useAxiosInstance from '@/lib/axios-instance';
import { useMutation } from '@tanstack/react-query';
import { useNavigate } from 'react-router-dom';

export interface TitleSchema
{
    title: string,
    description: string,
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

    onSuccess : async (response,param) => {
      console.log(response);
      navigate('/title-page-summary', {
        state :  {
          summary : await response,
          title: param.title,
          description: param.description,
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