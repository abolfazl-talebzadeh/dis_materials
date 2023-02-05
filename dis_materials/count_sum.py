from mrjob.job import MRJob

class MRCountSum(MRJob):

    def mapper(self, _, line):
        # line = line.strip() # remove leading and trailing whitespace
        # if line.find("From:") == 0:
        #     email_domain = line[line.find("@")+1:line.find(">")]
        #     if len(email_domain) == 0:
        #         email_domain == "empty"
        #     yield email_domain, 1
        if line.find("From: ")!=-1 and line.find("@")!=-1:
                tempList = line.rsplit("@")
                rstring=tempList[len(tempList)-1].strip()
                if rstring.find('>')>=0:
                    email=rstring[0:rstring.find('>')]
                elif rstring.find("(")>=0:
                    email=rstring[0:rstring.find('(')]
                elif rstring.find(")")>=0:
                    email=rstring[0:rstring.find(")")]
                yield email, 1
    def combiner(self, key, values):
        yield key, sum(values)
        
    def reducer(self, key, values):
        yield key, sum(values)


if __name__ == '__main__':
    MRCountSum.run()