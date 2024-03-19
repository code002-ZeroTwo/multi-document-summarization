import useGetSummaryByTitle from "../hooks/useGetSummaryByTitle";
import useGetTitles from "../hooks/useGetTitles";
import { Button } from "../ui/button";
import { Input } from "../ui/input";
import {
  Form,
  FormControl,
  FormField,
  FormItem,
  FormMessage,
} from "../ui/form"
import useGetTitlesByKeyword from "@/hooks/useGetTitlesByKeyword";
import { useLocation, useNavigate } from "react-router-dom"
import { useEffect } from "react";

const Home = () => {
  const { data, isLoading } = useGetTitles();
  const { onSubmit } = useGetSummaryByTitle();
  const {form, SubmitHandler}  = useGetTitlesByKeyword();
  const navigate = useNavigate();
  const location = useLocation();
 

  useEffect(() => {
    window.history.replaceState({}, '');
  },[])

  return (
    <>
      <div className="border-[5px] p-[2rem] border-primary mb-[40px] bg-secondary">
        <h1 className="font-bold text-[50px]  m-[20px] mt-[0]">
          Get The Summary By Keywords
        </h1>
        <p className="m-[20px]">
          First, enter the keyword. After clicking the 'Get titles' button, you
          will get the titles. Then, click on a title to get the generated
          summary.
        </p>

        <div >
          <Form {...form}>
            <form onSubmit={form.handleSubmit(SubmitHandler)} className="flex justify-center gap-[1rem]">
              <FormField
                control={form.control}
                name="query"
                render={({ field }) => (
                  <FormItem>
                    <FormControl>
                      <Input placeholder="Enter a keyword" className=" bg-white p-[20px]"  {...field} />
                    </FormControl>
                    <FormMessage />
                  </FormItem>
                )}
              />
              <Button type="submit" className="p-[20px]">Get titles</Button>
            </form>
          </Form>

          <div className="flex flex-col gap-[1rem] items-center mt-5">

            {!location.state?.titles
              ? ""
              : location.state?.titles?.map((title : any) => (
                  <Button
                    className="w-[60%] py-[2rem]"
                    key={title[0]}
                    onClick={() => {
                      navigate('/loading');
                      onSubmit({ title: title[0], description: title[1] });
                    }}
                  >
                    {title[0]}{" "}
                  </Button>
                ))} 
                  </div>
        </div>
      </div>

      <div>
        <h1 className="font-bold text-[50px]">
          Get The Summary Of Today's Hot Topics
        </h1>
        <p className=" m-[20px]">
          {" "}
          Click on one of the buttons to generate summary for the respective
          topic
        </p>

        <div className="flex flex-col gap-[1rem] items-center">
          {isLoading
            ? "Titles are loading..."
            : data?.titles?.map((title) => (
                <Button
                  className="w-[60%] py-[2rem]"
                  key={title[0]}
                  onClick={() => {
                    navigate('/loading');
                    onSubmit({ title: title[0], description: title[1] });
                  }}
                >
                  {title[0]}{" "}
                </Button>
              ))}
        </div>
      </div>
    </>
  );
};

export default Home;
