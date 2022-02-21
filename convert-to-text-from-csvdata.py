import pandas as pd
import os


def make_input_file_from_csv(infile, colname, writefile):
    df = pd.read_csv(infile)
    data_dict = df.to_dict()
    #print(data_dict[colname])
    with open(writefile, 'w') as the_file:
        for keyindex in data_dict[colname].keys():
            sentvalue = data_dict[colname][keyindex]
            print(sentvalue)
            the_file.write(str(str(sentvalue) + '\n'))
    the_file.close()

def make_tag_file_from_csv(infile, writefile):
    df = pd.read_csv(infile)
    #colnamelist = ["definition", "purpose", "process", "quantization", "finetune", "add-model", "add-data", "deploy", "studio"]
    with open(writefile, 'w') as the_file:
        for ind in df.index:
            rowvalue = ""
            value = int(df["definition"][ind])
            print(value)
            rowvalue = rowvalue + str(value)
            value = int(df["purpose"][ind])
            print(value)
            rowvalue = rowvalue + "," + str(value)
            value = int(df["process"][ind])
            print(value)
            rowvalue = rowvalue + "," + str(value)
            value = int(df["quantization"][ind])
            print(value)
            rowvalue = rowvalue + "," + str(value)
            value = int(df["finetune"][ind])
            print(value)
            rowvalue = rowvalue + "," + str(value)
            value = int(df["add-model"][ind])
            print(value)
            rowvalue = rowvalue + "," + str(value)
            value = int(df["add-data"][ind])
            print(value)
            rowvalue = rowvalue + "," + str(value)
            value = int(df["deploy"][ind])
            print(value)
            rowvalue = rowvalue + "," + str(value)
            value = int(df["studio"][ind])
            print(value)
            rowvalue = rowvalue + "," + str(value)
            the_file.write(str(str(rowvalue) + '\n'))
    the_file.close()

if __name__ == "__main__":
    tfp = os.path.dirname(os.path.abspath(__file__))
    filename1 = os.path.join(tfp, "helplabelledmergedcatraindata21feb22.csv")
    make_input_file_from_csv(filename1, "seq.in", "seq.in.txt")
    make_input_file_from_csv(filename1, "label", "label.txt")
    make_input_file_from_csv(filename1, "seq.out", "seq.out.txt")
    make_tag_file_from_csv(filename1, "tags.txt")

