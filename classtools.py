"Assorted class utilities and tools"
class AttrDisplay:
    def gatherAttrs(self):
        attrs=[]
        for key in sorted(self.__dict__):
            attrs.append('%s=%s' % (key, getattr(self, key)))
        return ','.join(attrs)

    def __str__(self):
        return '[%s: %s]' % (self.__class__.__name__, self.gatherAttrs())

if __name__=='__main__':
    class TopTest(AttrDisplay):
        count = 2

        def __init__(self):
            self.attr1 = TopTest.count
            self.attr2 = TopTest.count+1
            TopTest.count += 2

    class SubTest(TopTest):
        pass

    X = TopTest()
    print(X)
    print(SubTest.count)
    Y = SubTest()
    print(Y)
    print(SubTest.count)