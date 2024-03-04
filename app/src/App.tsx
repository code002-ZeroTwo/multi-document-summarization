import './App.css'
import useGetTitles from './hooks/useGetTitles'
import { Button } from './ui/button';

function App() {

  const {data, isLoading} = useGetTitles();
  return (
    <>
    <h1>Today's Hot Topics</h1>

    <div className='flex flex-col'>
    {isLoading ? 'Titles are loading' : data?.titles.map(title => <Button>{title}</Button>)}
    </div>
    </>
  )
}

export default App
