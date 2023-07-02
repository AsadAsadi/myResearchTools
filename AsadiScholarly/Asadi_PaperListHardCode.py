######################################################################
list_of_papers_khordad1402_3 = ["Determinants of customer loyalty dimensions: E-commerce context in emerging economy perspective",\
                                "Logistic service as a determinant of customer loyalty in e-commerce",\
                                "Effect of E-Service Quality on E-Customer Loyalty through E-Customers Satisfaction on E-Commerce Shopee Application",\
                                "Underlying factors influencing consumers' trust and loyalty in E-commerce",\
                                "The effects of the online customer experience on customer loyalty in e-retailers"]
list_of_years_khordad1402_3 = [2021,2020,2022,2020,2020]
#########################################################################
List_of_titles =list_of_papers_khordad1402_3
List_of_years =  list_of_years_khordad1402_3
#######################################################################
def Get_list_of_Papers_FromHarcodedList():
    if (len (List_of_titles) == len(List_of_years)):
        return List_of_titles,List_of_years
    else:
        msg = "Get_list_of_Papers_FromHarcodedList:: Mismatch in Hardcoded List len(List_of_years)= " +str(len(List_of_years)) + " but len (List_of_titles)= "+str(len (List_of_titles)) 
        raise Exception(msg)
    #################################################################
