
import time
import timeit
import datetime 
import traceback


#####################################################################

import Asadi_GeneralPaperSearcher
import LocalGPT.run_localGPT as run_localGPT
import LocalGPT.ingest as ingest

#####################################################################

TODAY = "1402-03-29"
TODAY_LATIN =  time.strftime("%Y-%m-%d")
start_date = '2018' 
end_date = '2024'

COMPLETED_JOBS = []


start_main_function_time = 0
selected_job_id = -1

#....................................................
def set_start_main_function_time(tim):
	global start_main_function_time
	start_main_function_time = tim
def get_start_main_function_time():
	return start_main_function_time
def remember_searching_date(todaay):
		global TODAY
		TODAY = todaay


############################################################################################	
def main_method_execute_once(conn_method, waiting_minutes, INTERACTIVE_MODE, TODAY_in, keywords, keywords_ABR, start_date, end_date, selected_task):
	# 1 means ask everything from commandline	
	DEBUG = 0

	start_run_once = timeit.default_timer()
	print("~"*50)
	print("main_method_execute_once DEBUG MODE= %s , INTERACTIVE_MODE = %s " % (DEBUG, INTERACTIVE_MODE))
	
	print("-----------------------len(keywords) = ",len(keywords))
	print("len(keywords_ABR) = ",len(keywords_ABR))
	print("\nkeywords = ",keywords)
	print("\nkeywords_ABR = ",keywords_ABR)
	print("~"*50)
	remember_searching_date(TODAY_in)

###############################################################################		
	while(len(COMPLETED_JOBS) == 0):
###############################################################################						
			#...............
			selected_task = int(input(" select 1) run GPT \n 2)search papers"))
			if(selected_task == 1):
				run_localGPT.main()
				COMPLETED_JOBS = ['gpt']
				pass
			if(selected_task == 2):
				path = "./LocalGPT/SOURCE_DOCUMENTS"
				Asadi_GeneralPaperSearcher.Level_1_Progress = 1.0
				print("before DownloadPapers_AccordingToHardCodedlList ..")
				Asadi_GeneralPaperSearcher.DownloadPapers_AccordingToHardCodedlList(dwn_dir= path)
				COMPLETED_JOBS = ['download']			
				ingest.main()
	
			print(".o."*20)
			print("COMPLETED_JOBS so far ...", COMPLETED_JOBS)
			so_far_run = timeit.default_timer()
			duration = so_far_run - start_run_once
			duration_from_begin = so_far_run - get_start_main_function_time()
			print("duration so far % s seconds, i.e %s minutes " % (duration , duration / 60))
			print("duration_from_begin so far % s seconds, i.e %s minutes, i.e %s hours " % (duration_from_begin , duration_from_begin / 60, duration_from_begin / 3600))
			current_time = datetime.datetime.now()
			# printing current time in Tehran
			print ("The current time in Tehran is : ",current_time)		
			print(".o."*20)			
	
	stop_run = timeit.default_timer()
	duration = stop_run - start_run_once
	duration_from_begin = stop_run - get_start_main_function_time()	
	print("duration_from_begin so far % s seconds, i.e %s minutes " % (duration_from_begin , duration_from_begin / 60))
	print("main method rune_once finished in % s seconds, i.e %s minutes " % (duration , duration / 60))

##########################################################################

def main_method():

	global TODAY
	global start_date 
	global end_date 
	
	RUNED_once = False
	
	set_start_main_function_time(timeit.default_timer())
	print("-"*10)
	conn_method =  "none"
	
	
	keywords = [""]
	keywords_ABR = [""] 
	INTERACTIVE_MODE = 1
	keyword_generation_mode = -1	
	keyword_generation_mode = 0
	if (keyword_generation_mode == 0):
			keywords = ["?"]
			keywords_ABR = ["?"]	   
					
	print("@@@@@@@@@@@@@@@@@len(keywords) = ",len(keywords))
	print("len(keywords_ABR) = ",len(keywords_ABR))
	print("\nkeywords = ",keywords)
	print("\nkeywords_ABR = ",keywords_ABR)
	if(INTERACTIVE_MODE == 1):
		current_time = datetime.datetime.now()
		# printing current time in Tehran
		print ("The current time in Tehran is : ",current_time)
		print("-"*30)
		print("TODAY_LATIN ",TODAY_LATIN)
		print("Default value for TODAY ", TODAY)
		new_day = input ("Enter TODAY's date, if default value is OK, just press enter ")
		if (new_day is None or len(new_day) < 2):
			print("TODAY do not changed")
		else:
			TODAY = new_day
			
	
	selected_job_id = 21
		
		
	print("today is ", TODAY)
	print("conn_method = ", conn_method)
	print(" start_main_function_time ", get_start_main_function_time())
	print("~"*50)
	waiting_minutes = 1
	while (not RUNED_once):
		try:
			#conn_method, waiting_minutes, INTERACTIVE_MODE, TODAY, keywords, keywords_ABR, start_date, end_date, selected_task
			main_method_execute_once(conn_method,waiting_minutes, INTERACTIVE_MODE, TODAY, keywords, keywords_ABR, start_date, end_date, selected_job_id)
			RUNED_once = True
			break;	
		except Exception as expn:
									
			print ("error before RUNED_once", expn)
			print("\n\n\n")
			traceback.print_tb(expn.__traceback__)
			print("\n\n\n")
			
			
			current_time = timeit.default_timer()
			Elapsed_time_from_start = (current_time - get_start_main_function_time()) / 60
			print("Elapsed_time_from_start(minutes) =%s, === %s hours " % (Elapsed_time_from_start, Elapsed_time_from_start / 60))			

	stop = timeit.default_timer()
	duration = stop - get_start_main_function_time()
	
	print("start_date ", start_date)
	print("end_date", end_date)		
	
	print("\n main loop finished in % s seconds,= i.e %s minutes, = %s hours " % (duration , duration / 60, duration / 3600))
		
	current_time = datetime.datetime.now()
	# printing current time in Tehran
	print ("The current time in Tehran is : ",current_time)
	
if __name__ == '__main__':
	main_method()