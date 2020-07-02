import os
import difflib
import csv
import re
import re
print(os.getcwd())
class info :
    def __init__(self,question,answer):
        self.question =question
        self.answear = answer
        self.science = open('subjects/science.txt','a')
        self.vocab = open('subjects/vocab.txt','a')
        self.equation = open('subjects/equations.txt', 'a')
        self.others = open('subjects/others.txt', 'a')
        self.huo = re.compile(r'(\w+\s+\w+)+').split(self.question)


    def question_answear(self,subject):
        if subject == str(3):
            if self.huo:
                self.v = str(self.question + ' ').replace(' ', '_')
                self.science.write(str(self.v))
                self.science.write(' ; {}'.format(str(self.answear)))
                self.science.write('\n')
            else:
                self.science.write(str(self.question))
                self.science.write(' ; {}'.format(str(self.answear)))
                self.science.write('\n')
        elif subject == str(4):
            if self.huo:
                self.v = str(self.question + ' ').replace(' ', '_')
                self.vocab.write(str(self.v))
                self.vocab.write(' ; {}'.format(str(self.answear)))
                self.vocab.write('\n')
            else:
                self.vocab.write(str(self.question))
                self.vocab.write(' ; {}'.format(str(self.answear)))
                self.vocab.write('\n')
        elif subject == str(1):
            if self.huo:
                self.v=str(self.question + ' ').replace(' ','_')
                self.equation.write(str(self.v))
                self.equation.write(' ; {}'.format(str(self.answear)))
                self.equation.write('\n')
            else:
                self.equation.write(str(self.question))
                self.equation.write(' ; {}'.format(str(self.answear)))
                self.equation.write('\n')

        elif subject == str(2):
            if self.huo:
                self.v = str(self.question + ' ').replace(' ', '_')
                self.others.write(str(self.v))
                self.others.write(' ; {}'.format(str(self.answear)))
                self.others.write('\n')
            else:
                self.others.write(str(self.question))
                self.others.write(' ; {}'.format(str(self.answear)))
                self.others.write('\n')
        else:
            print('UNAVAILABLE DIRECTORY')
        self.equation.close()
        self.others.close()
        self.science.close()
        self.vocab.close()


class show:
    def __init__(self,question):
        self.question = question
        self.science = open('/Users/ivy_nova/importent-python-projects/School_Proj/subjects/science.txt', 'r')
        self.vocab = open('subjects/vocab.txt', 'r')
        self.equation = open('subjects/equations.txt', 'r')
        self.others = open('subjects/others.txt', 'r')
        self.d = []
        self.lst = []
        self.jake = []
        self.empty = []
        self.num = (1, 2, 3, 4,)
        self.spaces = re.compile(r'{}'.format(self.question))
        self.lst.append(self.question)
        self.forloop = None
        self.i = None
        self.v = None
        self.t = None
        self.x = None
        self.stop = None
        self.ik = None
        self.mass = re.compile(r'(.*)[\s];[\w\s,\'\[\]!?]*[\s]+{}[\s]*[\s\w,\'\[\]!?]*[\s]*'.format(self.question),re.IGNORECASE)
        self.vass = re.compile(r'(.*)[\s];[\w*\s,]*,(\s{})+'.format(self.question,re.IGNORECASE))
        self.sars = re.compile(r'({})\s;[\w*,\s]*,( \w* ),+'.format(self.question,re.IGNORECASE))
        self.grass = re.compile(r'(.*)[\s];[\w*\s,]*,(\s\w*)*,(\s{})'.format(self.question, re.IGNORECASE))
        self.frass = re.compile(r'({})[\s];[\w*\s,]*,(\s\w*)*,(\s.*)'.format(self.question, re.IGNORECASE))
        self.v1text = re.compile(r'(\w*)[\s]+(\w*)[\s]+[\s]+[\s]*;[\s][\w]*')
        self.v12text = re.compile(r'(\w*\s)*\s(\w*\s)*\s;[\s][\w*]')
        self.mt = re.compile(r'[^.\w\d\D\W]')
        self.huo = re.compile(r'\s+').split(self.question)
        self.science_lst = []
        self.others_lst = []
        self.vocab_lst = []
        self.equations_lst = []




    def result(self,subject):


        g = str(self.question + ' ').replace(' ', '_')
        science  = self.science.read()
        vocab = self.vocab.read()
        equations = self.equation.read()
        others = self.others.read()
        lst = self.lst[0].split()
        self.kdd = []
        for i in self.v1text.findall(science):
            for i in i:
                self.science_lst.append(i)
        for i in self.v1text.findall(others):
            for i in i:
                self.others_lst.append(i)
        for i in self.v1text.findall(equations):
            for i in i:
                self.equations_lst.append(i)
        for i in self.v1text.findall(vocab):
            for i in i:
                self.vocab_lst.append(i)

        maybe_science = difflib.get_close_matches(self.question,self.science_lst , cutoff=0.00001)
        maybe_science2 = difflib.get_close_matches(self.huo, self.science_lst, cutoff=0.0000001)

        maybe_vocab = difflib.get_close_matches(self.question, self.vocab_lst, cutoff=0.0000001)
        maybe_vocab2 = difflib.get_close_matches(self.huo,self.vocab_lst, cutoff=0.000005)

        maybe_others = difflib.get_close_matches(self.question, self.others_lst, cutoff=0.0001)
        maybe_others2 = difflib.get_close_matches(self.huo, self.others_lst, cutoff=0.0001)

        maybe_equations= difflib.get_close_matches(self.question, self.equations_lst, cutoff=0.0001)
        maybe_equations2= difflib.get_close_matches(self.huo, self.equations_lst, cutoff=0.0001)

        #print(maybe_vocab)
        self.crass = re.compile(r'(.*)[\s];[\w\s,\'\[\]!?]*[\s]+{}[\s]*[\s\w,\'\[\]!?]*[\s]*'.format(maybe_vocab),re.IGNORECASE)
        lsteg = []
        data = csv.reader(science)

        #print(lsteg)

        # print(lst)

        #print(equations)
        if subject == str(3):

            for self.forloop in lst:
                #print(self.forloop)
                #print(self.spaces.findall(read))
                #print(science.split())
                #print(type(self.question))

                pass

            if g in self.science_lst or self.forloop in self.science_lst:

                text = re.compile(r'{}[\s*][\s*][\s\w*]*;[\s](.*)'.format(str(g)))
                vtext = re.compile(r'{}[\s*][\s*][\s\w*]*;[\s](.*)'.format(str(self.question)))
                for self.ik in text.findall(str(science)):
                    print('Answer is:', self.ik)

                if self.ik == None:
                    for i in vtext.findall(str(science)):
                        print('Answer is:', i)


            else:
                if maybe_science or maybe_science2:
                    inb = input('Did you mean {} [y/n]: '.format(maybe_science[0]))
                    if inb == 'y':
                        text = re.compile(r'{}[\s*][\s*][\s\w*]*;[\s](.*)'.format(str(maybe_science[0])))
                        vstext = re.compile(r'{}[\s*][\s*][\s\w*]*;[\s](.*)'.format(str(self.question)))
                        vtext = re.compile(r'{}[\s*][\s*][\s\w*]*;[\s](.*)'.format(str(maybe_science[0])))
                        for self.ik in text.findall(str(science)):
                            print('Answer is:', self.ik)

                        if self.ik == None:
                            for i in vtext.findall(str(science)):
                                print('Answer is:', i)
                        if maybe_science == None :
                            text = re.compile(r'{}[\s*][\s*][\s\w*]*;[\s](.*)'.format(str(maybe_science2[0])))
                            vstext = re.compile(r'{}[\s*][\s*][\s\w*]*;[\s](.*)'.format(str(self.question)))
                            vtext = re.compile(r'{}[\s*][\s*][\s\w*]*;[\s](.*)'.format(str(maybe_science2[0])))
                            for self.ik in text.findall(str(science)):
                                print('Answer is:', self.ik)

                            if self.ik == None:
                                 for i in vtext.findall(str(science)):
                                     print('Answer is:', i)
                else:

                        print('QUESTION NOT FOUND IN DATA BASE')
                        print('')
                        hal = input('1:Show file\n2:Add a Question: ')
                        if hal == '1':
                             print('\n',science)


                        elif hal == '2':
                            answer = input('insert the answer to the question: ')

                            info(self.question, answer).question_answear(str(3))

                        exit()
        elif subject == str(1):
            for self.forloop in lst:
                # print(self.forloop)
                # print(self.spaces.findall(read))
                # print(read.split())
                # print(type(self.question))
                pass
            if self.huo:

                g = str(self.question + ' ').replace(' ', '_')
            # print(str(self.question + ' ').replace(' ', '_'))
            else:
                g = self.forloop

            if g in self.equations_lst or self.forloop in self.equations_lst:
                print(self.equations_lst)

                text = re.compile(r'{}[\s*][\s*][\s\w*]*;[\s](.*)'.format(str(g)))
                vstext = re.compile(r'{}[\s*][\s*][\s\w*]*;[\s](.*)'.format(str(self.question)))
                vtext = re.compile(r'{}[\s*][\s\w*]*;[\s](.*)'.format(str(self.question)))
                for self.ik in text.findall(str(equations)):
                    print('Answer is:', self.ik)
                if self.ik == None:

                    for i in vstext.findall(str(equations)):

                        print('Answer is:', i)

            else:
                if maybe_equations :


                    inb = input('Did you mean {} [y/n]: '.format(maybe_equations[0]))
                    if inb == 'y':
                        text = re.compile(r'{}[\s*][\s*][\s\w*]*;[\s](.*)'.format(str(maybe_equations[0])))

                        for self.ik in text.findall(equations):
                            print('Answer is:', self.ik)
                            if self.ik == None:
                                vtext = re.compile(r'{}[\s*][\s*][\s\w*]*;[\s](.*)'.format(maybe_equations[0]))

                                for i in vtext.findall(str(equations)):
                                   print('Answer is:', i)
                    else:
                        print('QUESTION NOT FOUND IN DATA BASE')
                        hal = input('1:Show file\n2:Add a Question: ')
                        if hal == '1':
                            print('\n', equations)


                        elif hal == '2':
                                answer = input('insert the answer to the question: ')

                                info(self.question, answer).question_answear(str(1))
                else:
                    print('QUESTION NOT FOUND IN DATA BASE')
                    hal = input('1:Show file\n2:Add a Question: ')
                    if hal == '1':
                        print('\n', equations)


                    elif hal == '2':
                            answer = input('insert the answer to the question: ')

                            info(self.question, answer).question_answear(str(1))


                    exit()
        elif subject == str(4):

            for self.forloop in lst:
                # print(self.forloop)
                # print(self.spaces.findall(read))
                # print(read.split())
                # print(type(self.question))
                pass

            if self.forloop in self.vocab_lst or g in self.vocab_lst:

                text = re.compile(r'{}[\s*][\s\w*]*;[\s](.*)'.format(str(self.question)))
                inpu = input('1:Get for a word\n2:Get a whole sentence\n3:synynom\n4:Antynom\nAnswer: ')
                if inpu == str(1):
                    for i in self.mass.findall(str(vocab).replace('_',' ')):
                       # print(self.mass.findall(str(vocab).replace('_', ' ')))
                        print('Answer is:', i)


                elif inpu == str(2):
                    if g in vocab.split() or self.forloop in vocab.split():

                        text = re.compile(r'{}[\s*][\s*][\s\w*]*;[\s](.*)'.format(str(g)))
                        vstext = re.compile(r'{}[\s*][\s*][\s\w*]*;[\s](.*)'.format(str(self.question)))
                        vtext = re.compile(r'{}[\s*][\s*][\s\w*]*;[\s](.*)'.format(str(self.question)))
                        for self.ik in text.findall(str(vocab)):
                            print('Answer is:', self.ik)

                        if self.ik == None:
                                for i in vstext.findall(str(vocab)):
                                    print('Answer is:', i)

                elif inpu == str(3):
                    for i in self.vass.findall(str(vocab).replace('_',' ')):
                       # print(self.mass.findall(str(vocab).replace('_', ' ')))
                        print('Synynom of {} is : '.format(self.question), i)
                    for i in self.sars.findall(str(vocab).replace('_',' ')):
                       # print(self.mass.findall(str(vocab).replace('_', ' ')))
                        print('Synynom of {} is : '.format(self.question), i)


                elif inpu == str(4):
                     for i in self.grass.findall(str(vocab).replace('_',' ')):
                       # print(self.mass.findall(str(vocab).replace('_', ' ')))
                         print('Antynom of {} is : '.format(self.question), i[0])
                     for i in self.frass.findall(str(vocab).replace('_',' ')):
                       # print(self.mass.findall(str(vocab).replace('_', ' ')))
                         print('Antynom of {} is : '.format(self.question), i[2:])


            else:
                if maybe_vocab or maybe_vocab2:
                    inb = input('Did you mean {} [y/n]: '.format(maybe_vocab[0]))
                    if inb == 'y':
                        text = re.compile(r'{}[\s*][\s*][\s\w*]*;[\s](.*)'.format(str(maybe_vocab[0])))
                        vtext = re.compile(r'{}[\s*][\s*][\s\w*]*;[\s](.*)'.format(str(maybe_vocab[0])))
                        for self.ik in text.findall(str(vocab)):
                            print('Answer is:', self.ik)
                        if self.ik == None:
                               for i in vtext.findall(str(vocab)):
                                   print('Answer is:', i)
                else:
                    print('QUESTION NOT FOUND IN DATA BASE')
                    hal = input('1:Show file\n2:Add a Question: ')
                    if hal == '1':
                        print('\n', vocab)


                    elif hal == '2':
                        answer = input('insert the answer to the question: ')

                        info(self.question, answer).question_answear(str(4))

                exit()
        elif subject == str(2):
            for self.forloop in lst:
                # print(self.forloop)
                # print(self.spaces.findall(read))
                # print(read.split())
                # print(type(self.question))
                pass

            if self.huo:

                g = str(self.question + ' ').replace(' ', '_')
            # print(str(self.question + ' ').replace(' ', '_'))
            else:
                g = self.forloop

            if g in others.split() or self.forloop in others.split():

                text = re.compile(r'{}[\s*][\s*][\s\w*]*;[\s](.*)'.format(str(g)))
                vstext = re.compile(r'{}[\s*][\s*][\s\w*]*;[\s](.*)'.format(str(self.question)))
                vtext = re.compile(r'{}[\s*][\s*][\s\w*]*;[\s](.*)'.format(str(self.question)))
                for self.ik in text.findall(str(others)):
                    print('Answer is:', self.ik)
                if self.ik == None:
                    for i in vtext.findall(str(others)):
                        print('Answer is:', i)
            else:

                inb = input('Did you mean {} [y/n]: '.format(maybe_others[0]))
                if inb == 'y':
                    text = re.compile(r'{}[\s*][\s*][\s\w*]*;[\s](.*)'.format(str(maybe_others[0])))
                    vtext = re.compile(r'{}[\s*][\s*][\s\w*]*;[\s](.*)'.format(str(maybe_others[0])))
                    for self.ik in text.findall(str(others)):
                        print('Answer is:', self.ik)
                    for i in self.ik:
                        if i == self.empty:
                            for i in vtext.findall(str(others)):
                                print('Answer is:', i)
                else:


                    hal = input('1:Show file\n2:Add a Question: ')
                    if hal == '1':
                        print('\n', others)


                    elif hal == '2':
                        answer = input('insert the answer to the question: ')

                        info(self.question, answer).question_answear(str(2))
        elif subject == str(5):
            for self.forloop in lst:
                # print(self.forloop)
                # print(self.spaces.findall(read))
                # print(read.split())
                # print(type(self.question))
                pass
            text = re.compile(r'{}[\s*][\s*][\s\w*]*;[\s](.*)'.format(str(self.question)))


            if self.forloop in equations.split():


                for self.i in text.findall(str(equations)):

                    if self.i in text.findall(str(equations)):
                        print('answer is: ',self.i,'\nfrom directory equations')
            if self.forloop in others.split():
                for self.x in text.findall(str(others)):

                    if self.x in text.findall(str(others)):
                        print('answer is: ',self.x,'\nfrom directory others')
            if self.forloop in science.split():
                for self.v in text.findall(str(science)):

                    if self.v in text.findall(str(science)):
                        print('answer is: ',self.v,'\nfrom directory science')
            if self.forloop in vocab.split():
                for self.t in text.findall(str(vocab)):

                    if self.t in text.findall(str(vocab)):
                        print('answer is: ',self.t,'\nfrom directory vocab')
