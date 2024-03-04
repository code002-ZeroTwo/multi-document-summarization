import useGetSummaryByTitle from '../hooks/useGetSummaryByTitle';
import useGetTitles from '../hooks/useGetTitles'
import { Button } from '../ui/button';


const Home = () => {
    const {data, isLoading} = useGetTitles();
    const {onSubmit} = useGetSummaryByTitle();
  
    return (
      <div>
      <h1 className='font-bold text-[320px]'>Today's Hot Topics</h1>
  
      <div style={{
        display: 'flex',
        flexDirection: 'column',
        gap: '0.4rem',
      }}>
      {isLoading ? 'Titles are loading...' : data?.titles?.map(title => <Button  key={title} onClick={() => {onSubmit({title})}}>{title}</Button>)}
      </div>
      </div>
    )
}

export default Home
