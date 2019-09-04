from PyPDF2 import PdfFileReader, PdfFileWriter
import sys
def unlock(i):
    with open(input('Enter PDFfile name to crack : ') , 'rb') as input_file, \
        open('cracked.pdf', 'wb') as output_file:
        reader = PdfFileReader(input_file)
        writer = PdfFileWriter()
        while True:
            print("Trying password : " +str(i))
            sys.stdout.write('\x1b[1A')
            sys.stdout.write('\x1b[2K')
            if i%10000==0:
                print(i)
            if str(reader.decrypt(str(i)))=='1':
                pswd=i
                for i in range(reader.getNumPages()):
                    writer.addPage(reader.getPage(i))

                writer.write(output_file)
                exit('password cracked :' +str(pswd))
            i+=1
if __name__ == '__main__':
    unlock(0)
    
  
