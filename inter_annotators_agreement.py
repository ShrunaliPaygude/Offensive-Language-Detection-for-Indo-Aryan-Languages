import pandas as pd
from sklearn.metrics import cohen_kappa_score

def main():

    files = ['./Inter_Annotator_Data/mrinal_Shrunali.xlsx', './Inter_Annotator_Data/shrunali.xlsx']
    file_contents = []
    #prefix= "Annotated Data//"
    for file in files:
        file_content = pd.read_excel(file)
        file_contents.append(file_content)
        agreements=[]
    for annotator in range(0, len(file_contents), 2):
        # Here the step was 1 by default, it should be 2 to compare
        # between the "Class" column of both the datasets
        agreement = cohen_kappa_score(list(file_contents[annotator]['Class'][:100]), list(file_contents[annotator + 1]['Class'][:100]))
        agreements.append(agreement)
        #print(agreement)
    print("Average agreement: ", sum(agreements)/len(agreements))



def main2():
    # check len of invalid, offensive and non-offensive
    files = ['./Inter_Annotator_Data/mrinal_Shrunali.xlsx', './Inter_Annotator_Data/shrunali.xlsx', './Inter_Annotator_Data/mayuresh.xlsx']
    #prefix="Annotated Data//"
    file_contents=pd.DataFrame()
    # What if duplicates?
    duplicate=0
    for file in files:
        file_content=pd.read_excel(file)
        if duplicate%2==0:
            file_contents.append(file_content)
        else:
            file_contents.append(file_content[100:]) # need to append after 100th
        duplicate+=1
    #print(len(file_contents))
    #print(file_contents['Class'].unique())
    file_contents = file_contents[file_contents.Class != 'invalid']
    print(len(file_contents[file_contents['Class'] == 'offensive']))
    print(len(file_contents[file_contents['Class'] == 'not offensive']))






if __name__ == '__main__':
    #main2()
    main()



