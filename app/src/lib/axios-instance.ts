import axios from 'axios';
import { BASE_API_URL } from './constants';

const axiosInstance = axios.create({
  baseURL: `${BASE_API_URL}`,
  headers: {
    accept: 'application/json',
    'Access-Control-Allow-Origin' : '*',
    'Content-Type': 'application/json',
  },
});

const useAxiosInstance = () => {
  return axiosInstance
}

export default useAxiosInstance;
