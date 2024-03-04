import { KEYS } from '@/constants/keys';
import useAxiosInstance from '@/lib/axios-instance'
import { useQuery } from '@tanstack/react-query'

export interface TitleListType
{
  titles: string[]
}


const useGetTitles = () => {
  const axiosInstance = useAxiosInstance();
  return (
    useQuery({
      queryKey: [KEYS.titleList],
      queryFn: async() : Promise<TitleListType> => {
        const response = await axiosInstance.get('');
        return response?.data;
      }
    }

    )
  )
}

export default useGetTitles
