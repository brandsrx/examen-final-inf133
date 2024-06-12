def render_restaruant_list(restaruants):
    return [
        {
            "id":restaruant.id,
           "name":restaruant.name,
          "address":restaruant.address,
          "city":restaruant.city,
          "phone":restaruant.phone,
          "description":restaruant.description,
          "rating":restaruant.rating
        
        }
        for restaruant in restaruants
    ]


def render_restaruant_detail(restaruant):
    return {
       "id":restaruant.id,
           "name":restaruant.name,
          "address":restaruant.address,
          "city":restaruant.city,
          "phone":restaruant.phone,
          "description":restaruant.description,
          "rating":restaruant.rating
    }
