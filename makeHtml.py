#Make html images from png plots

class HtmlImageMaker():
    
    def __init__(self,outFileName):

        self._imageNames = []
        self._outFile = open(outFileName,'w')

    @staticmethod
    def makeHeader(outFile):
        outFile.write('<!DOCTYPE html>\n')
        outFile.write('<html>\n')
        outFile.write('<body>\n\n')
        
    @staticmethod
    def makeFooter(outFile):
        outFile.write('\n<body>\n')
        outFile.write('<html>\n')

    def addImages(self):

        for image in self._imageNames:
            # self._outFile.write('<div class="floated_img">\n')
            # self._outFile.write('\t<img src="'+image+'" alt="alphaT">\n')
            # self._outFile.write('\t<p>'+image+'<p>\n')
            # self._outFile.write('</div>\n')

            self._outFile.write('<a href="'+image+'">\n')
            self._outFile.write('\t<img width="400px" src="'+image+'"/>\n')
            #self._outFile.write('\t<p>'+image+'<p>\n')
            self._outFile.write('</a>\b')

        pass

    def appendImage(self,image):
        self._imageNames.append(image)

    def makeHtmlFile(self):
        self.makeHeader(self._outFile)
        self.addImages()
        self.makeFooter(self._outFile)
             
if __name__=='__main__':

    import glob
    import os
    from Core.Parser import parser

    parser.add_argument('-i','--inputDir', help="input directory")
    parser.add_argument('-t','--imageType', help="image type", default='png')

    opt = parser.parse_args()
    #
    # print os.walk(opt.inputDir)
    #
    # for dirPath,dirNames,fileNames in os.walk(opt.inputDir):
    #     print dirPath,dirNames,fileNames
    #     print '\n'
    #
    # exit()

    if not opt.inputDir:
        print 'give input directory with -i'
        exit()

    for dirPath,dirNames,fileNames in os.walk(opt.inputDir):
        if len(fileNames)==0: continue
        htmlImageMaker = HtmlImageMaker(os.path.join(dirPath,'index.html'))
        for image in glob.glob(os.path.join(dirPath,'*.'+opt.imageType)): 
            htmlImageMaker.appendImage(image.split('/')[-1])
        htmlImageMaker.makeHtmlFile()
