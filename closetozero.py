def closetozero(ts):
      if ts==[]:
          return None
      else:
          p=[]
          for i in ts :
              p.append(abs(i))
          if (-1*min(p) in ts ) and (min(p) in ts) :
            return min(p)
          elif (-1*min(p) in ts ) and not (min(p) in ts) :
              return -1*min(p)
          else :
              return min(p)

print(closetozero([-9,8,-2,-2,7]))