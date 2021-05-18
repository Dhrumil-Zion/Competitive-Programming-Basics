def timeInWords(h, m):
    li_hr = ["","one","two","three","four","five","six",
            "seven","eight","nine","ten","eleven","twelev"]
    lis_min = ["o' clock","one","two","three","four","five","six","seven","eight","nine",              "ten","eleven", "twelve", "thirteen", "fourteen", "quarter", "sixteen",                  "seventeen", "eighteen", "nineteen","twenty","twenty one","twenty two",                  "twenty three","twenty four","twenty five","twenty six","twenty seven",                  "twenty eight","twenty nine","half"]

    if int(m) == 0:
        return ("{} {}".format(li_hr[h],lis_min[0]))
    elif int(m)>0 and int(m)<10:
        return ("{} minute past {}".format(lis_min[m],li_hr[h]))
    elif int(m)>9 and int(m)<=30:
        if int(m) in [15, 30]:
            return ("{} past {}".format(lis_min[m],li_hr[h]))
        return ("{} minutes past {}".format(lis_min[m],li_hr[h]))
    elif int(m)>30 and int(m)<60:
        if int(m) == 45:
            return ("{} to {}".format(lis_min[60-m],li_hr[h+1]))
        return ("{} minutes to {}".format(lis_min[60-m],li_hr[h+1]))   