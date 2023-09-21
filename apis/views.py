from rest_framework import viewsets

from .serializers import DistrictSerializer,ProvinceSerializer, LocalGovernmentSerializer
from .models import District, Province, LocalGovernment

# Create your views here.

class ProvinceViewSet(viewsets.ModelViewSet):
    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer

class DistrictViewSet(viewsets.ModelViewSet):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer

class LocalGovernmentViewSet(viewsets.ModelViewSet):
    data =  [
    {
      "id": 1,
      "lgid": 10101,
      
      "lgname_en": "Phaktanglung Rural Mun",
      "lgname_np": "फक्ताङलुङ गाउँपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 1,
        "did": 101,
        
        "district_en": "Taplejung",
        "district_np": "ताप्लेजुङ"
      }
    },
    {
      "id": 2,
      "lgid": 10102,
      
      "lgname_en": "Mikwakhola Rural Mun",
      "lgname_np": "मिक्वाखोला गाउँपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 1,
        "did": 101,
        
        "district_en": "Taplejung",
        "district_np": "ताप्लेजुङ"
      }
    },
    {
      "id": 3,
      "lgid": 10103,
      
      "lgname_en": "Meringden Rural Mun",
      "lgname_np": "मेरिङदेन गाउँपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 1,
        "did": 101,
        
        "district_en": "Taplejung",
        "district_np": "ताप्लेजुङ"
      }
    },
    {
      "id": 4,
      "lgid": 10104,
      
      "lgname_en": "Maiwakhola Rural Mun",
      "lgname_np": "मैवाखोला गाउँपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 1,
        "did": 101,
        
        "district_en": "Taplejung",
        "district_np": "ताप्लेजुङ"
      }
    },
    {
      "id": 5,
      "lgid": 10105,
      
      "lgname_en": "Aathraitribeni Rural Mun",
      "lgname_np": "आठराई त्रिवेणी गाउँपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 1,
        "did": 101,
        
        "district_en": "Taplejung",
        "district_np": "ताप्लेजुङ"
      }
    },
    {
      "id": 6,
      "lgid": 10106,
      
      "lgname_en": "Phungling Municipality",
      "lgname_np": "फुङलिङ नगरपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 1,
        "did": 101,
        
        "district_en": "Taplejung",
        "district_np": "ताप्लेजुङ"
      }
    },
    {
      "id": 7,
      "lgid": 10107,
      
      "lgname_en": "Pathivara Yangwarak Rural Mun",
      "lgname_np": "पाथीभरा याङवरक गाउँपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 1,
        "did": 101,
        
        "district_en": "Taplejung",
        "district_np": "ताप्लेजुङ"
      }
    },
    {
      "id": 8,
      "lgid": 10108,
      
      "lgname_en": "Sirijangha Rural Mun",
      "lgname_np": "सिरीजङ्घा गाउँपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 1,
        "did": 101,
        
        "district_en": "Taplejung",
        "district_np": "ताप्लेजुङ"
      }
    },
    {
      "id": 9,
      "lgid": 10109,
      
      "lgname_en": "Sidingba Rural Mun",
      "lgname_np": "सिदिङ्वा गाउँपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 1,
        "did": 101,
        
        "district_en": "Taplejung",
        "district_np": "ताप्लेजुङ"
      }
    },
    {
      "id": 10,
      "lgid": 10201,
      
      "lgname_en": "Bhotkhola Rural Mun",
      "lgname_np": "भोटखोला गाउँपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 2,
        "did": 102,
        
        "district_en": "Sankhuwasabha",
        "district_np": "संखुवासभा"
      }
    },
    {
      "id": 11,
      "lgid": 10202,
      
      "lgname_en": "Makalu Rural Mun",
      "lgname_np": "मकालु गाउँपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 2,
        "did": 102,
        
        "district_en": "Sankhuwasabha",
        "district_np": "संखुवासभा"
      }
    },
    {
      "id": 12,
      "lgid": 10203,
      
      "lgname_en": "Silichong Rural Mun",
      "lgname_np": "सिलीचोङ गाउँपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 2,
        "did": 102,
        
        "district_en": "Sankhuwasabha",
        "district_np": "संखुवासभा"
      }
    },
    {
      "id": 13,
      "lgid": 10204,
      
      "lgname_en": "Chichila Rural Mun",
      "lgname_np": "चिचिला गाउँपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 2,
        "did": 102,
        
        "district_en": "Sankhuwasabha",
        "district_np": "संखुवासभा"
      }
    },
    {
      "id": 14,
      "lgid": 10205,
      
      "lgname_en": "Savapokhari Rural Mun",
      "lgname_np": "सभापोखरी गाउँपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 2,
        "did": 102,
        
        "district_en": "Sankhuwasabha",
        "district_np": "संखुवासभा"
      }
    },
    {
      "id": 15,
      "lgid": 10206,
      
      "lgname_en": "Khandbari Municipality",
      "lgname_np": "खाँदवारी नगरपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 2,
        "did": 102,
        
        "district_en": "Sankhuwasabha",
        "district_np": "संखुवासभा"
      }
    },
    {
      "id": 16,
      "lgid": 10207,
      
      "lgname_en": "Panchkhapan Municipality",
      "lgname_np": "पाँचखपन नगरपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 2,
        "did": 102,
        
        "district_en": "Sankhuwasabha",
        "district_np": "संखुवासभा"
      }
    },
    {
      "id": 17,
      "lgid": 10208,
      
      "lgname_en": "Chainpur Municipality",
      "lgname_np": "चैनपुर नगरपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 2,
        "did": 102,
        
        "district_en": "Sankhuwasabha",
        "district_np": "संखुवासभा"
      }
    },
    {
      "id": 18,
      "lgid": 10209,
      
      "lgname_en": "Madi Municipality",
      "lgname_np": "मादी नगरपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 2,
        "did": 102,
        
        "district_en": "Sankhuwasabha",
        "district_np": "संखुवासभा"
      }
    },
    {
      "id": 19,
      "lgid": 10210,
      
      "lgname_en": "Dharmadevi Municipality",
      "lgname_np": "धर्मदेवी नगरपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 2,
        "did": 102,
        
        "district_en": "Sankhuwasabha",
        "district_np": "संखुवासभा"
      }
    },
    {
      "id": 20,
      "lgid": 10301,
      
      "lgname_en": "Khumbupasanglhamu Rural Mun",
      "lgname_np": "खुम्वु पासाङल्हमु गाउँपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 3,
        "did": 103,
        
        "district_en": "Solukhumbu",
        "district_np": "सोलुखुम्बु"
      }
    },
    {
      "id": 21,
      "lgid": 10302,
      
      "lgname_en": "Mahakulung Rural Mun",
      "lgname_np": "माहाकुलुङ गाउँपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 3,
        "did": 103,
        
        "district_en": "Solukhumbu",
        "district_np": "सोलुखुम्बु"
      }
    },
    {
      "id": 22,
      "lgid": 10303,
      
      "lgname_en": "Sotang Rural Mun",
      "lgname_np": "सोताङ गाउँपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 3,
        "did": 103,
        
        "district_en": "Solukhumbu",
        "district_np": "सोलुखुम्बु"
      }
    },
    {
      "id": 23,
      "lgid": 10304,
      
      "lgname_en": "Mapya Dudhkoshi Rural Mun",
      "lgname_np": "माप्य दुधकोशी गाउँपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 3,
        "did": 103,
        
        "district_en": "Solukhumbu",
        "district_np": "सोलुखुम्बु"
      }
    },
    {
      "id": 24,
      "lgid": 10305,
      
      "lgname_en": "Thulung Dudhkoshi Rural Mun",
      "lgname_np": "थुलुङ दुधकोशी गाउँपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 3,
        "did": 103,
        
        "district_en": "Solukhumbu",
        "district_np": "सोलुखुम्बु"
      }
    },
    {
      "id": 25,
      "lgid": 10306,
      
      "lgname_en": "Nechasalyan Rural Mun",
      "lgname_np": "नेचासल्यान गाउँपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 3,
        "did": 103,
        
        "district_en": "Solukhumbu",
        "district_np": "सोलुखुम्बु"
      }
    },
    {
      "id": 26,
      "lgid": 10307,
      
      "lgname_en": "Solududhkunda Municipality",
      "lgname_np": "सोलुदुधकुण्ड नगरपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 3,
        "did": 103,
        
        "district_en": "Solukhumbu",
        "district_np": "सोलुखुम्बु"
      }
    },
    {
      "id": 27,
      "lgid": 10308,
      
      "lgname_en": "Likhupike Rural Mun",
      "lgname_np": "लिखु पिके गाउँपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 3,
        "did": 103,
        
        "district_en": "Solukhumbu",
        "district_np": "सोलुखुम्बु"
      }
    },
    {
      "id": 28,
      "lgid": 10401,
      
      "lgname_en": "Chishankhugadhi Rural Mun",
      "lgname_np": "चिशंखुगढी गाउँपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 4,
        "did": 104,
        
        "district_en": "Okhaldhunga",
        "district_np": "ओखलढुंगा"
      }
    },
    {
      "id": 29,
      "lgid": 10402,
      
      "lgname_en": "Siddhicharan Municipality",
      "lgname_np": "सिद्दिचरण नगरपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 4,
        "did": 104,
        
        "district_en": "Okhaldhunga",
        "district_np": "ओखलढुंगा"
      }
    },
    {
      "id": 30,
      "lgid": 10403,
      
      "lgname_en": "Molung Rural Mun",
      "lgname_np": "मोलुङ गाउँपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 4,
        "did": 104,
        
        "district_en": "Okhaldhunga",
        "district_np": "ओखलढुंगा"
      }
    },
    {
      "id": 31,
      "lgid": 10404,
      
      "lgname_en": "Khijidemba Rural Mun",
      "lgname_np": "खिजिदेम्बा गाउँपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 4,
        "did": 104,
        
        "district_en": "Okhaldhunga",
        "district_np": "ओखलढुंगा"
      }
    },
    {
      "id": 32,
      "lgid": 10405,
      
      "lgname_en": "Likhu Rural Mun",
      "lgname_np": "लिखु गाउँपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 4,
        "did": 104,
        
        "district_en": "Okhaldhunga",
        "district_np": "ओखलढुंगा"
      }
    },
    {
      "id": 33,
      "lgid": 10406,
      
      "lgname_en": "Champadevi Rural Mun",
      "lgname_np": "चम्पादेवी गाउँपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 4,
        "did": 104,
        
        "district_en": "Okhaldhunga",
        "district_np": "ओखलढुंगा"
      }
    },
    {
      "id": 34,
      "lgid": 10407,
      
      "lgname_en": "Sunkoshi Rural Mun",
      "lgname_np": "सुनकोशी गाउँपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 4,
        "did": 104,
        
        "district_en": "Okhaldhunga",
        "district_np": "ओखलढुंगा"
      }
    },
    {
      "id": 35,
      "lgid": 10408,
      
      "lgname_en": "Manebhanjyang Rural Mun",
      "lgname_np": "मानेभञ्याङ गाउँपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 4,
        "did": 104,
        
        "district_en": "Okhaldhunga",
        "district_np": "ओखलढुंगा"
      }
    },
    {
      "id": 36,
      "lgid": 10501,
      
      "lgname_en": "Kepilasgadhi Rural Mun",
      "lgname_np": "केपिलासगढी गाउँपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 5,
        "did": 105,
        
        "district_en": "Khotang",
        "district_np": "खोटाङ"
      }
    },
    {
      "id": 37,
      "lgid": 10502,
      
      "lgname_en": "Aiselukharka Rural Mun",
      "lgname_np": "ऐसेलुखर्क गाउँपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 5,
        "did": 105,
        
        "district_en": "Khotang",
        "district_np": "खोटाङ"
      }
    },
    {
      "id": 38,
      "lgid": 10503,
      
      "lgname_en": "Rawa Besi Rural Mun",
      "lgname_np": "रावा बेसी गाउँपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 5,
        "did": 105,
        
        "district_en": "Khotang",
        "district_np": "खोटाङ"
      }
    },
    {
      "id": 39,
      "lgid": 10504,
      
      "lgname_en": "Halesituwachung Municipality",
      "lgname_np": "हलेसी तुवाचुङ नगरपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 5,
        "did": 105,
        
        "district_en": "Khotang",
        "district_np": "खोटाङ"
      }
    },
    {
      "id": 40,
      "lgid": 10505,
      
      "lgname_en": "Diktel Rupakot Majhuwagadhi Municipality",
      "lgname_np": "दिक्तेल रुपाकोट मझुवागढी नगरपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 5,
        "did": 105,
        
        "district_en": "Khotang",
        "district_np": "खोटाङ"
      }
    },
    {
      "id": 41,
      "lgid": 10506,
      
      "lgname_en": "Sakela Rural Mun",
      "lgname_np": "साकेला गाउँपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 5,
        "did": 105,
        
        "district_en": "Khotang",
        "district_np": "खोटाङ"
      }
    },
    {
      "id": 42,
      "lgid": 10507,
      
      "lgname_en": "Diprung Chuichumma Rural Mun",
      "lgname_np": "दिप्रुङ चुइचुम्मा गाउँपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 5,
        "did": 105,
        
        "district_en": "Khotang",
        "district_np": "खोटाङ"
      }
    },
    {
      "id": 43,
      "lgid": 10508,
      
      "lgname_en": "Khotehang Rural Mun",
      "lgname_np": "खोटेहाङ गाउँपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 5,
        "did": 105,
        
        "district_en": "Khotang",
        "district_np": "खोटाङ"
      }
    },
    {
      "id": 44,
      "lgid": 10509,
      
      "lgname_en": "Jantedhunga Rural Mun",
      "lgname_np": "जन्तेढुंगा गाउँपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 5,
        "did": 105,
        
        "district_en": "Khotang",
        "district_np": "खोटाङ"
      }
    },
    {
      "id": 45,
      "lgid": 10510,
      
      "lgname_en": "Barahapokhari Rural Mun",
      "lgname_np": "वराहपोखरी गाउँपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 5,
        "did": 105,
        
        "district_en": "Khotang",
        "district_np": "खोटाङ"
      }
    },
    {
      "id": 46,
      "lgid": 10601,
      
      "lgname_en": "Shadananda Municipality",
      "lgname_np": "षडानन्द नगरपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 6,
        "did": 106,
        
        "district_en": "Bhojpur",
        "district_np": "भोजपुर"
      }
    },
    {
      "id": 47,
      "lgid": 10602,
      
      "lgname_en": "Salpasilichho Rural Mun",
      "lgname_np": "साल्पासिलिछो गाउँपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 6,
        "did": 106,
        
        "district_en": "Bhojpur",
        "district_np": "भोजपुर"
      }
    },
    {
      "id": 48,
      "lgid": 10603,
      
      "lgname_en": "Temkemaiyum Rural Mun",
      "lgname_np": "टेम्केमैयुङ गाउँपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 6,
        "did": 106,
        
        "district_en": "Bhojpur",
        "district_np": "भोजपुर"
      }
    },
    {
      "id": 49,
      "lgid": 10604,
      
      "lgname_en": "Bhojpur Municipality",
      "lgname_np": "भोजपुर नगरपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 6,
        "did": 106,
        
        "district_en": "Bhojpur",
        "district_np": "भोजपुर"
      }
    },
    {
      "id": 50,
      "lgid": 10605,
      
      "lgname_en": "Arun Rural Mun",
      "lgname_np": "अरुण गाउँपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 6,
        "did": 106,
        
        "district_en": "Bhojpur",
        "district_np": "भोजपुर"
      }
    },
    {
      "id": 51,
      "lgid": 10606,
      
      "lgname_en": "Pauwadungma Rural Mun",
      "lgname_np": "पौवादुङमा गाउँपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 6,
        "did": 106,
        
        "district_en": "Bhojpur",
        "district_np": "भोजपुर"
      }
    },
    {
      "id": 52,
      "lgid": 10607,
      
      "lgname_en": "Ramprasadrai Rural Mun",
      "lgname_np": "रामप्रसाद राई गाउँपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 6,
        "did": 106,
        
        "district_en": "Bhojpur",
        "district_np": "भोजपुर"
      }
    },
    {
      "id": 53,
      "lgid": 10608,
      
      "lgname_en": "Hatuwagadhi Rural Mun",
      "lgname_np": "हतुवागढी गाउँपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 6,
        "did": 106,
        
        "district_en": "Bhojpur",
        "district_np": "भोजपुर"
      }
    },
    {
      "id": 54,
      "lgid": 10609,
      
      "lgname_en": "Aamchowk Rural Mun",
      "lgname_np": "आमचोक गाउँपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 6,
        "did": 106,
        
        "district_en": "Bhojpur",
        "district_np": "भोजपुर"
      }
    },
    {
      "id": 55,
      "lgid": 10701,
      
      "lgname_en": "Mahalaxmi Municipality",
      "lgname_np": "महालक्ष्मी नगरपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 7,
        "did": 107,
        
        "district_en": "Dhankuta",
        "district_np": "धनकुटा"
      }
    },
    {
      "id": 56,
      "lgid": 10702,
      
      "lgname_en": "Pakhribas Municipality",
      "lgname_np": "पाख्रिबास नगरपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 7,
        "did": 107,
        
        "district_en": "Dhankuta",
        "district_np": "धनकुटा"
      }
    },
    {
      "id": 57,
      "lgid": 10703,
      
      "lgname_en": "Chhatharjorpati Rural Mun",
      "lgname_np": "छथर जोरपाटी गाउँपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 7,
        "did": 107,
        
        "district_en": "Dhankuta",
        "district_np": "धनकुटा"
      }
    },
    {
      "id": 58,
      "lgid": 10704,
      
      "lgname_en": "Dhankuta Municipality",
      "lgname_np": "धनकुटा नगरपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 7,
        "did": 107,
        
        "district_en": "Dhankuta",
        "district_np": "धनकुटा"
      }
    },
    {
      "id": 59,
      "lgid": 10705,
      
      "lgname_en": "Shahidbhumi Rural Mun",
      "lgname_np": "सहिदभूमि गाउँपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 7,
        "did": 107,
        
        "district_en": "Dhankuta",
        "district_np": "धनकुटा"
      }
    },
    {
      "id": 60,
      "lgid": 10706,
      
      "lgname_en": "Sangurigadhi Rural Mun",
      "lgname_np": "साँगुरीगढी गाउँपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 7,
        "did": 107,
        
        "district_en": "Dhankuta",
        "district_np": "धनकुटा"
      }
    },
    {
      "id": 61,
      "lgid": 10707,
      
      "lgname_en": "Choubise Rural Mun",
      "lgname_np": "चौविसे गाउँपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 7,
        "did": 107,
        
        "district_en": "Dhankuta",
        "district_np": "धनकुटा"
      }
    },
    {
      "id": 62,
      "lgid": 10801,
      
      "lgname_en": "Aathrai Rural Mun",
      "lgname_np": "आठराई गाउँपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 8,
        "did": 108,
        
        "district_en": "Tehrathum",
        "district_np": "तेहथुम"
      }
    },
    {
      "id": 63,
      "lgid": 10802,
      
      "lgname_en": "Phedap Rural Mun",
      "lgname_np": "फेदाप गाउँपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 8,
        "did": 108,
        
        "district_en": "Tehrathum",
        "district_np": "तेहथुम"
      }
    },
    {
      "id": 64,
      "lgid": 10803,
      
      "lgname_en": "Menchhayayem Rural Mun",
      "lgname_np": "मेन्छयायेम गाउँपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 8,
        "did": 108,
        
        "district_en": "Tehrathum",
        "district_np": "तेहथुम"
      }
    },
    {
      "id": 65,
      "lgid": 10804,
      
      "lgname_en": "Myanglung Municipality",
      "lgname_np": "म्याङलुङ नगरपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 8,
        "did": 108,
        
        "district_en": "Tehrathum",
        "district_np": "तेहथुम"
      }
    },
    {
      "id": 66,
      "lgid": 10805,
      
      "lgname_en": "Laligurans Municipality",
      "lgname_np": "लालीगुराँस नगरपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 8,
        "did": 108,
        
        "district_en": "Tehrathum",
        "district_np": "तेहथुम"
      }
    },
    {
      "id": 67,
      "lgid": 10806,
      
      "lgname_en": "Chhathar Rural Mun",
      "lgname_np": "छथर गाउँपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 8,
        "did": 108,
        
        "district_en": "Tehrathum",
        "district_np": "तेहथुम"
      }
    },
    {
      "id": 68,
      "lgid": 10901,
      
      "lgname_en": "Yangwarak Rural Mun",
      "lgname_np": "याङवरक गाउँपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 9,
        "did": 109,
        
        "district_en": "Panchthar",
        "district_np": "पाँचथर"
      }
    },
    {
      "id": 69,
      "lgid": 10902,
      
      "lgname_en": "Hilihang Rural Mun",
      "lgname_np": "हिलिहाङ गाउँपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 9,
        "did": 109,
        
        "district_en": "Panchthar",
        "district_np": "पाँचथर"
      }
    },
    {
      "id": 70,
      "lgid": 10903,
      
      "lgname_en": "Phalelung Rural Mun",
      "lgname_np": "फालेलुङ गाउँपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 9,
        "did": 109,
        
        "district_en": "Panchthar",
        "district_np": "पाँचथर"
      }
    },
    {
      "id": 71,
      "lgid": 10904,
      
      "lgname_en": "Phidim Municipality",
      "lgname_np": "फिदिम नगरपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 9,
        "did": 109,
        
        "district_en": "Panchthar",
        "district_np": "पाँचथर"
      }
    },
    {
      "id": 72,
      "lgid": 10905,
      
      "lgname_en": "Phalgunanda Rural Mun",
      "lgname_np": "फाल्गुनन्द गाउँपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 9,
        "did": 109,
        
        "district_en": "Panchthar",
        "district_np": "पाँचथर"
      }
    },
    {
      "id": 73,
      "lgid": 10906,
      
      "lgname_en": "Kummayak Rural Mun",
      "lgname_np": "कुम्मायक गाउँपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 9,
        "did": 109,
        
        "district_en": "Panchthar",
        "district_np": "पाँचथर"
      }
    },
    {
      "id": 74,
      "lgid": 10907,
      
      "lgname_en": "Tumwewa Rural Mun",
      "lgname_np": "तुम्बेवा गाउँपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 9,
        "did": 109,
        
        "district_en": "Panchthar",
        "district_np": "पाँचथर"
      }
    },
    {
      "id": 75,
      "lgid": 10908,
      
      "lgname_en": "Miklajung Rural Mun",
      "lgname_np": "मिक्लाजुङ गाउँपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 9,
        "did": 109,
        
        "district_en": "Panchthar",
        "district_np": "पाँचथर"
      }
    },
    {
      "id": 76,
      "lgid": 11001,
      
      "lgname_en": "Maijogmai Rural Mun",
      "lgname_np": "माईजोगमाई गाउँपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 10,
        "did": 110,
        
        "district_en": "Ilam",
        "district_np": "ईलाम"
      }
    },
    {
      "id": 77,
      "lgid": 11002,
      
      "lgname_en": "Sandakpur Rural Mun",
      "lgname_np": "सन्दकपुर गाउँपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 10,
        "did": 110,
        
        "district_en": "Ilam",
        "district_np": "ईलाम"
      }
    },
    {
      "id": 78,
      "lgid": 11003,
      
      "lgname_en": "Ilam Municipality",
      "lgname_np": "ईलाम नगरपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 10,
        "did": 110,
        
        "district_en": "Ilam",
        "district_np": "ईलाम"
      }
    },
    {
      "id": 79,
      "lgid": 11004,
      
      "lgname_en": "Deumai Municipality",
      "lgname_np": "देउमाई नगरपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 10,
        "did": 110,
        
        "district_en": "Ilam",
        "district_np": "ईलाम"
      }
    },
    {
      "id": 80,
      "lgid": 11005,
      
      "lgname_en": "Phakphokthum Rural Mun",
      "lgname_np": "फाकफोकथुम गाउँपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 10,
        "did": 110,
        
        "district_en": "Ilam",
        "district_np": "ईलाम"
      }
    },
    {
      "id": 81,
      "lgid": 11006,
      
      "lgname_en": "Mansebung Rural Mun",
      "lgname_np": "माङसेबुङ गाउँपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 10,
        "did": 110,
        
        "district_en": "Ilam",
        "district_np": "ईलाम"
      }
    },
    {
      "id": 82,
      "lgid": 11007,
      
      "lgname_en": "Chulachuli Rural Mun",
      "lgname_np": "चुलाचुली गाउँपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 10,
        "did": 110,
        
        "district_en": "Ilam",
        "district_np": "ईलाम"
      }
    },
    {
      "id": 83,
      "lgid": 11008,
      
      "lgname_en": "Mai Municipality",
      "lgname_np": "माई नगरपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 10,
        "did": 110,
        
        "district_en": "Ilam",
        "district_np": "ईलाम"
      }
    },
    {
      "id": 84,
      "lgid": 11009,
      
      "lgname_en": "Suryodaya Municipality",
      "lgname_np": "सूर्योदय नगरपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 10,
        "did": 110,
        
        "district_en": "Ilam",
        "district_np": "ईलाम"
      }
    },
    {
      "id": 85,
      "lgid": 11010,
      
      "lgname_en": "Rong Rural Mun",
      "lgname_np": "रोङ गाउँपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 10,
        "did": 110,
        
        "district_en": "Ilam",
        "district_np": "ईलाम"
      }
    },
    {
      "id": 86,
      "lgid": 11101,
      
      "lgname_en": "Mechinagar Municipality",
      "lgname_np": "मेचीनगर नगरपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 11,
        "did": 111,
        
        "district_en": "Jhapa",
        "district_np": "झापा"
      }
    },
    {
      "id": 87,
      "lgid": 11102,
      
      "lgname_en": "Buddhashanti Rural Mun",
      "lgname_np": "बुद्धशान्ति गाउँपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 11,
        "did": 111,
        
        "district_en": "Jhapa",
        "district_np": "झापा"
      }
    },
    {
      "id": 88,
      "lgid": 11103,
      
      "lgname_en": "Arjundhara Municipality",
      "lgname_np": "अर्जुनधारा नगरपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 11,
        "did": 111,
        
        "district_en": "Jhapa",
        "district_np": "झापा"
      }
    },
    {
      "id": 89,
      "lgid": 11104,
      
      "lgname_en": "Kankai Municipality",
      "lgname_np": "कन्काई नगरपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 11,
        "did": 111,
        
        "district_en": "Jhapa",
        "district_np": "झापा"
      }
    },
    {
      "id": 90,
      "lgid": 11105,
      
      "lgname_en": "Shivasatakshi Municipality",
      "lgname_np": "शिवशताक्षी नगरपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 11,
        "did": 111,
        
        "district_en": "Jhapa",
        "district_np": "झापा"
      }
    },
    {
      "id": 91,
      "lgid": 11106,
      
      "lgname_en": "Kamal Rural Mun",
      "lgname_np": "कमल गाउँपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 11,
        "did": 111,
        
        "district_en": "Jhapa",
        "district_np": "झापा"
      }
    },
    {
      "id": 92,
      "lgid": 11107,
      
      "lgname_en": "Damak Municipality",
      "lgname_np": "दमक नगरपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 11,
        "did": 111,
        
        "district_en": "Jhapa",
        "district_np": "झापा"
      }
    },
    {
      "id": 93,
      "lgid": 11108,
      
      "lgname_en": "Gauradaha Municipality",
      "lgname_np": "गौरादह नगरपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 11,
        "did": 111,
        
        "district_en": "Jhapa",
        "district_np": "झापा"
      }
    },
    {
      "id": 94,
      "lgid": 11109,
      
      "lgname_en": "Gaurigunj Rural Mun",
      "lgname_np": "गौरीगंज गाउँपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 11,
        "did": 111,
        
        "district_en": "Jhapa",
        "district_np": "झापा"
      }
    },
    {
      "id": 95,
      "lgid": 11110,
      
      "lgname_en": "Jhapa Rural Mun",
      "lgname_np": "झापा गाउँपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 11,
        "did": 111,
        
        "district_en": "Jhapa",
        "district_np": "झापा"
      }
    },
    {
      "id": 96,
      "lgid": 11111,
      
      "lgname_en": "Bahradashi Rural Mun",
      "lgname_np": "बाह्रदशी गाउँपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 11,
        "did": 111,
        
        "district_en": "Jhapa",
        "district_np": "झापा"
      }
    },
    {
      "id": 97,
      "lgid": 11112,
      
      "lgname_en": "Birtamod Municipality",
      "lgname_np": "विर्तामोड नगरपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 11,
        "did": 111,
        
        "district_en": "Jhapa",
        "district_np": "झापा"
      }
    },
    {
      "id": 98,
      "lgid": 11113,
      
      "lgname_en": "Haldibari Rural Mun",
      "lgname_np": "हल्दिवारी गाउँपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 11,
        "did": 111,
        
        "district_en": "Jhapa",
        "district_np": "झापा"
      }
    },
    {
      "id": 99,
      "lgid": 11114,
      
      "lgname_en": "Bhadrapur Municipality",
      "lgname_np": "भद्रपुर नगरपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 11,
        "did": 111,
        
        "district_en": "Jhapa",
        "district_np": "झापा"
      }
    },
    {
      "id": 100,
      "lgid": 11115,
      
      "lgname_en": "Kachankawal Rural Mun",
      "lgname_np": "कचनकवल गाउँपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 11,
        "did": 111,
        
        "district_en": "Jhapa",
        "district_np": "झापा"
      }
    },
    {
      "id": 101,
      "lgid": 11201,
      
      "lgname_en": "Miklajung Rural Mun",
      "lgname_np": "मिक्लाजुङ गाउँपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 12,
        "did": 112,
        
        "district_en": "Morang",
        "district_np": "मोरंग"
      }
    },
    {
      "id": 102,
      "lgid": 11202,
      
      "lgname_en": "Letang Municipality",
      "lgname_np": "लेटाङ नगरपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 12,
        "did": 112,
        
        "district_en": "Morang",
        "district_np": "मोरंग"
      }
    },
    {
      "id": 103,
      "lgid": 11203,
      
      "lgname_en": "Kerabari Rural Mun",
      "lgname_np": "केरावारी गाउँपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 12,
        "did": 112,
        
        "district_en": "Morang",
        "district_np": "मोरंग"
      }
    },
    {
      "id": 104,
      "lgid": 11204,
      
      "lgname_en": "Sundarharaicha Municipality",
      "lgname_np": "सुन्दरहरैचा नगरपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 12,
        "did": 112,
        
        "district_en": "Morang",
        "district_np": "मोरंग"
      }
    },
    {
      "id": 105,
      "lgid": 11205,
      
      "lgname_en": "Belbari Municipality",
      "lgname_np": "बेलवारी नगरपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 12,
        "did": 112,
        
        "district_en": "Morang",
        "district_np": "मोरंग"
      }
    },
    {
      "id": 106,
      "lgid": 11206,
      
      "lgname_en": "Kanepokhari Rural Mun",
      "lgname_np": "कानेपोखरी गाउँपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 12,
        "did": 112,
        
        "district_en": "Morang",
        "district_np": "मोरंग"
      }
    },
    {
      "id": 107,
      "lgid": 11207,
      
      "lgname_en": "Patharisanishchare Municipality",
      "lgname_np": "पथरी शनिश्चरे नगरपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 12,
        "did": 112,
        
        "district_en": "Morang",
        "district_np": "मोरंग"
      }
    },
    {
      "id": 108,
      "lgid": 11208,
      
      "lgname_en": "Urlabari Municipality",
      "lgname_np": "उर्लावारी नगरपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 12,
        "did": 112,
        
        "district_en": "Morang",
        "district_np": "मोरंग"
      }
    },
    {
      "id": 109,
      "lgid": 11209,
      
      "lgname_en": "Ratuwamai Municipality",
      "lgname_np": "रतुवामाई नगरपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 12,
        "did": 112,
        
        "district_en": "Morang",
        "district_np": "मोरंग"
      }
    },
    {
      "id": 110,
      "lgid": 11210,
      
      "lgname_en": "Sunawarshi Municipality",
      "lgname_np": "सुनवर्षि नगरपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 12,
        "did": 112,
        
        "district_en": "Morang",
        "district_np": "मोरंग"
      }
    },
    {
      "id": 111,
      "lgid": 11211,
      
      "lgname_en": "Rangeli Municipality",
      "lgname_np": "रंगेली नगरपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 12,
        "did": 112,
        
        "district_en": "Morang",
        "district_np": "मोरंग"
      }
    },
    {
      "id": 112,
      "lgid": 11212,
      
      "lgname_en": "Gramthan Rural Mun",
      "lgname_np": "ग्रामथान गाउँपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 12,
        "did": 112,
        
        "district_en": "Morang",
        "district_np": "मोरंग"
      }
    },
    {
      "id": 113,
      "lgid": 11213,
      
      "lgname_en": "Budhiganga Rural Mun",
      "lgname_np": "बुढीगंगा गाउँपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 12,
        "did": 112,
        
        "district_en": "Morang",
        "district_np": "मोरंग"
      }
    },
    {
      "id": 114,
      "lgid": 11214,
      
      "lgname_en": "Biratnagar Metro",
      "lgname_np": "विराटनगर महानगरपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 12,
        "did": 112,
        
        "district_en": "Morang",
        "district_np": "मोरंग"
      }
    },
    {
      "id": 115,
      "lgid": 11215,
      
      "lgname_en": "Katahari Rural Mun",
      "lgname_np": "कटहरी गाउँपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 12,
        "did": 112,
        
        "district_en": "Morang",
        "district_np": "मोरंग"
      }
    },
    {
      "id": 116,
      "lgid": 11216,
      
      "lgname_en": "Dhanapalthan Rural Mun",
      "lgname_np": "धनपालथान गाउँपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 12,
        "did": 112,
        
        "district_en": "Morang",
        "district_np": "मोरंग"
      }
    },
    {
      "id": 117,
      "lgid": 11217,
      
      "lgname_en": "Jahada Rural Mun",
      "lgname_np": "जहदा गाउँपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 12,
        "did": 112,
        
        "district_en": "Morang",
        "district_np": "मोरंग"
      }
    },
    {
      "id": 118,
      "lgid": 11301,
      
      "lgname_en": "Dharan Sub-Metro",
      "lgname_np": "धरान उपमहानगरपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 13,
        "did": 113,
        
        "district_en": "Sunsari",
        "district_np": "सुनसरी"
      }
    },
    {
      "id": 119,
      "lgid": 11302,
      
      "lgname_en": "Barahachhetra Municipality",
      "lgname_np": "बराहक्षेत्र नगरपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 13,
        "did": 113,
        
        "district_en": "Sunsari",
        "district_np": "सुनसरी"
      }
    },
    {
      "id": 120,
      "lgid": 11303,
      
      "lgname_en": "Koshi Rural Mun",
      "lgname_np": "कोशी गाउँपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 13,
        "did": 113,
        
        "district_en": "Sunsari",
        "district_np": "सुनसरी"
      }
    },
    {
      "id": 121,
      "lgid": 11304,
      
      "lgname_en": "Bhokraha Narsingh Rural Mun",
      "lgname_np": "भोक्राहा नरसिंह गाउँपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 13,
        "did": 113,
        
        "district_en": "Sunsari",
        "district_np": "सुनसरी"
      }
    },
    {
      "id": 122,
      "lgid": 11305,
      
      "lgname_en": "Ramdhuni Municipality",
      "lgname_np": "रामधुनी नगरपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 13,
        "did": 113,
        
        "district_en": "Sunsari",
        "district_np": "सुनसरी"
      }
    },
    {
      "id": 123,
      "lgid": 11306,
      
      "lgname_en": "Itahari Sub-Metro",
      "lgname_np": "ईटहरी उपमहानगरपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 13,
        "did": 113,
        
        "district_en": "Sunsari",
        "district_np": "सुनसरी"
      }
    },
    {
      "id": 124,
      "lgid": 11307,
      
      "lgname_en": "Duhabi Municipality",
      "lgname_np": "दुहवी नगरपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 13,
        "did": 113,
        
        "district_en": "Sunsari",
        "district_np": "सुनसरी"
      }
    },
    {
      "id": 125,
      "lgid": 11308,
      
      "lgname_en": "Gadhi Rural Mun",
      "lgname_np": "गढी गाउँपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 13,
        "did": 113,
        
        "district_en": "Sunsari",
        "district_np": "सुनसरी"
      }
    },
    {
      "id": 126,
      "lgid": 11309,
      
      "lgname_en": "Inaruwa Municipality",
      "lgname_np": "ईनरुवा नगरपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 13,
        "did": 113,
        
        "district_en": "Sunsari",
        "district_np": "सुनसरी"
      }
    },
    {
      "id": 127,
      "lgid": 11310,
      
      "lgname_en": "Harinagar Rural Mun",
      "lgname_np": "हरिनगर गाउँपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 13,
        "did": 113,
        
        "district_en": "Sunsari",
        "district_np": "सुनसरी"
      }
    },
    {
      "id": 128,
      "lgid": 11311,
      
      "lgname_en": "Dewanganj Rural Mun",
      "lgname_np": "देवानगञ्ज गाउँपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 13,
        "did": 113,
        
        "district_en": "Sunsari",
        "district_np": "सुनसरी"
      }
    },
    {
      "id": 129,
      "lgid": 11312,
      
      "lgname_en": "Barju Rural Mun",
      "lgname_np": "बर्जु गाउँपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 13,
        "did": 113,
        
        "district_en": "Sunsari",
        "district_np": "सुनसरी"
      }
    },
    {
      "id": 130,
      "lgid": 11401,
      
      "lgname_en": "Belaka Municipality",
      "lgname_np": "वेलका नगरपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 14,
        "did": 114,
        
        "district_en": "Udaypur",
        "district_np": "उदयपुर"
      }
    },
    {
      "id": 131,
      "lgid": 11402,
      
      "lgname_en": "Chaudandigadhi Municipality",
      "lgname_np": "चौदण्डीगढी नगरपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 14,
        "did": 114,
        
        "district_en": "Udaypur",
        "district_np": "उदयपुर"
      }
    },
    {
      "id": 132,
      "lgid": 11403,
      
      "lgname_en": "Triyuga Municipality",
      "lgname_np": "त्रियुगा नगरपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 14,
        "did": 114,
        
        "district_en": "Udaypur",
        "district_np": "उदयपुर"
      }
    },
    {
      "id": 133,
      "lgid": 11404,
      
      "lgname_en": "Rautamai Rural Mun",
      "lgname_np": "रौतामाई गाउँपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 14,
        "did": 114,
        
        "district_en": "Udaypur",
        "district_np": "उदयपुर"
      }
    },
    {
      "id": 134,
      "lgid": 11405,
      
      "lgname_en": "Limchungbung Rural Mun",
      "lgname_np": "लिम्चुङ्बुङ गाउँपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 14,
        "did": 114,
        
        "district_en": "Udaypur",
        "district_np": "उदयपुर"
      }
    },
    {
      "id": 135,
      "lgid": 11406,
      
      "lgname_en": "Tapli Rural Mun",
      "lgname_np": "ताप्ली गाउँपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 14,
        "did": 114,
        
        "district_en": "Udaypur",
        "district_np": "उदयपुर"
      }
    },
    {
      "id": 136,
      "lgid": 11407,
      
      "lgname_en": "Katari Municipality",
      "lgname_np": "कटारी नगरपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 14,
        "did": 114,
        
        "district_en": "Udaypur",
        "district_np": "उदयपुर"
      }
    },
    {
      "id": 137,
      "lgid": 11408,
      
      "lgname_en": "Udayapurgadhi Rural Mun",
      "lgname_np": "उदयपुरगढी गाउँपालिका",
      "province": {
        "id": 1,
        "province_en": "Koshi Province",
        "province_np": "कोशी प्रदेश",
        
      },
      "district": {
        "id": 14,
        "did": 114,
        
        "district_en": "Udaypur",
        "district_np": "उदयपुर"
      }
    },
    {
      "id": 138,
      "lgid": 20101,
      
      "lgname_en": "Saptakoshi Municipality",
      "lgname_np": "सप्तकोशी नगरपालिका",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 15,
        "did": 201,
        
        "district_en": "Saptari",
        "district_np": "सप्तरी"
      }
    },
    {
      "id": 139,
      "lgid": 20102,
      
      "lgname_en": "Kanchanrup Municipality",
      "lgname_np": "कञ्चनरुप नगरपालिका",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 15,
        "did": 201,
        
        "district_en": "Saptari",
        "district_np": "सप्तरी"
      }
    },
    {
      "id": 140,
      "lgid": 20103,
      
      "lgname_en": "Agnisairkrishnasawaran Rural Mun",
      "lgname_np": "अग्निसाइर कृष्णासरवन गाउँपालिका",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 15,
        "did": 201,
        
        "district_en": "Saptari",
        "district_np": "सप्तरी"
      }
    },
    {
      "id": 141,
      "lgid": 20104,
      
      "lgname_en": "Rupani Rural Mun",
      "lgname_np": "रुपनी गाउँपालिका",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 15,
        "did": 201,
        
        "district_en": "Saptari",
        "district_np": "सप्तरी"
      }
    },
    {
      "id": 142,
      "lgid": 20105,
      
      "lgname_en": "Shambhunath Municipality",
      "lgname_np": "शम्भुनाथ नगरपालिका",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 15,
        "did": 201,
        
        "district_en": "Saptari",
        "district_np": "सप्तरी"
      }
    },
    {
      "id": 143,
      "lgid": 20106,
      
      "lgname_en": "Khadak Municipality",
      "lgname_np": "खडक नगरपालिका",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 15,
        "did": 201,
        
        "district_en": "Saptari",
        "district_np": "सप्तरी"
      }
    },
    {
      "id": 144,
      "lgid": 20107,
      
      "lgname_en": "Surunga Municipality",
      "lgname_np": "सुरुङ्‍गा नगरपालिका",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 15,
        "did": 201,
        
        "district_en": "Saptari",
        "district_np": "सप्तरी"
      }
    },
    {
      "id": 145,
      "lgid": 20108,
      
      "lgname_en": "Balanbihul Rural Mun",
      "lgname_np": "बलान-बिहुल गाउँपालिका",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 15,
        "did": 201,
        
        "district_en": "Saptari",
        "district_np": "सप्तरी"
      }
    },
    {
      "id": 146,
      "lgid": 20109,
      
      "lgname_en": "Bodebarsain Municipality",
      "lgname_np": "बोदेबरसाईन नगरपालिका",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 15,
        "did": 201,
        
        "district_en": "Saptari",
        "district_np": "सप्तरी"
      }
    },
    {
      "id": 147,
      "lgid": 20110,
      
      "lgname_en": "Dakneshwori Municipality",
      "lgname_np": "डाक्नेश्वरी नगरपालिका",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 15,
        "did": 201,
        
        "district_en": "Saptari",
        "district_np": "सप्तरी"
      }
    },
    {
      "id": 148,
      "lgid": 20111,
      
      "lgname_en": "Rajgadh Rural Mun",
      "lgname_np": "राजगढ गाउँपालिका",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 15,
        "did": 201,
        
        "district_en": "Saptari",
        "district_np": "सप्तरी"
      }
    },
    {
      "id": 149,
      "lgid": 20112,
      
      "lgname_en": "Bishnupur Rural Mun",
      "lgname_np": "बिष्णुपुर गाउँपालिका",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 15,
        "did": 201,
        
        "district_en": "Saptari",
        "district_np": "सप्तरी"
      }
    },
    {
      "id": 150,
      "lgid": 20113,
      
      "lgname_en": "Rajbiraj Municipality",
      "lgname_np": "राजविराज नगरपालिका",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 15,
        "did": 201,
        
        "district_en": "Saptari",
        "district_np": "सप्तरी"
      }
    },
    {
      "id": 151,
      "lgid": 20114,
      
      "lgname_en": "Mahadeva Rural Mun",
      "lgname_np": "महादेवा गाउँपालिका",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 15,
        "did": 201,
        
        "district_en": "Saptari",
        "district_np": "सप्तरी"
      }
    },
    {
      "id": 152,
      "lgid": 20115,
      
      "lgname_en": "Tirahut Rural Mun",
      "lgname_np": "तिरहुत गाउँपालिका",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 15,
        "did": 201,
        
        "district_en": "Saptari",
        "district_np": "सप्तरी"
      }
    },
    {
      "id": 153,
      "lgid": 20116,
      
      "lgname_en": "Hanumannagarkankalini Municipality",
      "lgname_np": "हनुमाननगर कङ्‌कालिनी नगरपालिका",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 15,
        "did": 201,
        
        "district_en": "Saptari",
        "district_np": "सप्तरी"
      }
    },
    {
      "id": 154,
      "lgid": 20117,
      
      "lgname_en": "Tilathikoiladi Rural Mun",
      "lgname_np": "तिलाठी कोईलाडी गाउँपालिका",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 15,
        "did": 201,
        
        "district_en": "Saptari",
        "district_np": "सप्तरी"
      }
    },
    {
      "id": 155,
      "lgid": 20118,
      
      "lgname_en": "Chhinnamasta Rural Mun",
      "lgname_np": "छिन्नमस्ता गाउँपालिका",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 15,
        "did": 201,
        
        "district_en": "Saptari",
        "district_np": "सप्तरी"
      }
    },
    {
      "id": 156,
      "lgid": 20201,
      
      "lgname_en": "Lahan Municipality",
      "lgname_np": "लहान नगरपालिका ",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 16,
        "did": 202,
        
        "district_en": "Siraha",
        "district_np": "सिराहा"
      }
    },
    {
      "id": 157,
      "lgid": 20202,
      
      "lgname_en": "Dhangadhimai Municipality",
      "lgname_np": "धनगढीमाई नगरपालिका ",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 16,
        "did": 202,
        
        "district_en": "Siraha",
        "district_np": "सिराहा"
      }
    },
    {
      "id": 158,
      "lgid": 20203,
      
      "lgname_en": "Golbazar Municipality",
      "lgname_np": "गोलबजार नगरपालिका ",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 16,
        "did": 202,
        
        "district_en": "Siraha",
        "district_np": "सिराहा"
      }
    },
    {
      "id": 159,
      "lgid": 20204,
      
      "lgname_en": "Mirchaiya Municipality",
      "lgname_np": "मिर्चैयाँ नगरपालिका ",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 16,
        "did": 202,
        
        "district_en": "Siraha",
        "district_np": "सिराहा"
      }
    },
    {
      "id": 160,
      "lgid": 20205,
      
      "lgname_en": "Karjanha Municipality",
      "lgname_np": "कर्जन्हा नगरपालिका ",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 16,
        "did": 202,
        
        "district_en": "Siraha",
        "district_np": "सिराहा"
      }
    },
    {
      "id": 161,
      "lgid": 20206,
      
      "lgname_en": "Kalyanpur Municipality",
      "lgname_np": "कल्याणपुर नगरपालिका ",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 16,
        "did": 202,
        
        "district_en": "Siraha",
        "district_np": "सिराहा"
      }
    },
    {
      "id": 162,
      "lgid": 20207,
      
      "lgname_en": "Naraha Rural Mun",
      "lgname_np": "नरहा गाउँपालिका ",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 16,
        "did": 202,
        
        "district_en": "Siraha",
        "district_np": "सिराहा"
      }
    },
    {
      "id": 163,
      "lgid": 20208,
      
      "lgname_en": "Bishnupur Rural Mun",
      "lgname_np": "विष्णुपुर गाउँपालिका ",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 16,
        "did": 202,
        
        "district_en": "Siraha",
        "district_np": "सिराहा"
      }
    },
    {
      "id": 164,
      "lgid": 20209,
      
      "lgname_en": "Anarma Rural Mun",
      "lgname_np": "अर्नमा गाउँपालिका",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 16,
        "did": 202,
        
        "district_en": "Siraha",
        "district_np": "सिराहा"
      }
    },
    {
      "id": 165,
      "lgid": 20210,
      
      "lgname_en": "Sukhipur Municipality",
      "lgname_np": "सुखीपुर नगरपालिका",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 16,
        "did": 202,
        
        "district_en": "Siraha",
        "district_np": "सिराहा"
      }
    },
    {
      "id": 166,
      "lgid": 20211,
      
      "lgname_en": "Laxmipurpatari Rural Mun",
      "lgname_np": "लक्ष्मीपुर पतारी गाउँपालिका ",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 16,
        "did": 202,
        
        "district_en": "Siraha",
        "district_np": "सिराहा"
      }
    },
    {
      "id": 167,
      "lgid": 20212,
      
      "lgname_en": "Sakhuwanankarkatti Rural Mun",
      "lgname_np": "सखुवानान्कारकट्टी गाउँपालिका",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 16,
        "did": 202,
        
        "district_en": "Siraha",
        "district_np": "सिराहा"
      }
    },
    {
      "id": 168,
      "lgid": 20213,
      
      "lgname_en": "Bhagwanpur Rural Mun",
      "lgname_np": "भगवानपुर गाउँपालिका ",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 16,
        "did": 202,
        
        "district_en": "Siraha",
        "district_np": "सिराहा"
      }
    },
    {
      "id": 169,
      "lgid": 20214,
      
      "lgname_en": "Nawarajpur Rural Mun",
      "lgname_np": "नवराजपुर गाउँपालिका",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 16,
        "did": 202,
        
        "district_en": "Siraha",
        "district_np": "सिराहा"
      }
    },
    {
      "id": 170,
      "lgid": 20215,
      
      "lgname_en": "Bariyapatti Rural Mun",
      "lgname_np": "बरियारपट्टी गाउँपालिका ",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 16,
        "did": 202,
        
        "district_en": "Siraha",
        "district_np": "सिराहा"
      }
    },
    {
      "id": 171,
      "lgid": 20216,
      
      "lgname_en": "Aurahi Rural Mun",
      "lgname_np": "औरही गाउँपालिका ",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 16,
        "did": 202,
        
        "district_en": "Siraha",
        "district_np": "सिराहा"
      }
    },
    {
      "id": 172,
      "lgid": 20217,
      
      "lgname_en": "Siraha Municipality",
      "lgname_np": "सिरहा नगरपालिका ",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 16,
        "did": 202,
        
        "district_en": "Siraha",
        "district_np": "सिराहा"
      }
    },
    {
      "id": 173,
      "lgid": 20301,
      
      "lgname_en": "Ganeshmancharnath Municipality",
      "lgname_np": "गणेशमान चारनाथ नगरपालिका",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 17,
        "did": 203,
        
        "district_en": "Dhanusha",
        "district_np": "धनुषा"
      }
    },
    {
      "id": 174,
      "lgid": 20302,
      
      "lgname_en": "Dhanushadham Municipality",
      "lgname_np": "धनुषाधाम नगरपालिका",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 17,
        "did": 203,
        
        "district_en": "Dhanusha",
        "district_np": "धनुषा"
      }
    },
    {
      "id": 175,
      "lgid": 20303,
      
      "lgname_en": "Mithila Municipality",
      "lgname_np": "मिथिला नगरपालिका",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 17,
        "did": 203,
        
        "district_en": "Dhanusha",
        "district_np": "धनुषा"
      }
    },
    {
      "id": 176,
      "lgid": 20304,
      
      "lgname_en": "Bateshwor Rural Mun",
      "lgname_np": "बटेश्वर गाउँपालिका ",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 17,
        "did": 203,
        
        "district_en": "Dhanusha",
        "district_np": "धनुषा"
      }
    },
    {
      "id": 177,
      "lgid": 20305,
      
      "lgname_en": "Kshireshwornath Municipality",
      "lgname_np": "क्षिरेश्वरनाथ नगरपालिका",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 17,
        "did": 203,
        
        "district_en": "Dhanusha",
        "district_np": "धनुषा"
      }
    },
    {
      "id": 178,
      "lgid": 20306,
      
      "lgname_en": "Laxminiya Rural Mun",
      "lgname_np": "लक्ष्मीनिया गाउँपालिका ",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 17,
        "did": 203,
        
        "district_en": "Dhanusha",
        "district_np": "धनुषा"
      }
    },
    {
      "id": 179,
      "lgid": 20307,
      
      "lgname_en": "Mithilabihari Municipality",
      "lgname_np": "मिथिला बिहारी नगरपालिका",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 17,
        "did": 203,
        
        "district_en": "Dhanusha",
        "district_np": "धनुषा"
      }
    },
    {
      "id": 180,
      "lgid": 20308,
      
      "lgname_en": "Hansapur Municipality",
      "lgname_np": "हंसपुर नगरपालिका",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 17,
        "did": 203,
        
        "district_en": "Dhanusha",
        "district_np": "धनुषा"
      }
    },
    {
      "id": 181,
      "lgid": 20309,
      
      "lgname_en": "Sabaila Municipality",
      "lgname_np": "सबैला नगरपालिका",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 17,
        "did": 203,
        
        "district_en": "Dhanusha",
        "district_np": "धनुषा"
      }
    },
    {
      "id": 182,
      "lgid": 20310,
      
      "lgname_en": "Shahidnagar Municipality",
      "lgname_np": "शहीदनगर नगरपालिका",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 17,
        "did": 203,
        
        "district_en": "Dhanusha",
        "district_np": "धनुषा"
      }
    },
    {
      "id": 183,
      "lgid": 20311,
      
      "lgname_en": "Kamala Municipality",
      "lgname_np": "कमला नगरपालिका",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 17,
        "did": 203,
        
        "district_en": "Dhanusha",
        "district_np": "धनुषा"
      }
    },
    {
      "id": 184,
      "lgid": 20312,
      
      "lgname_en": "Janaknandini Rural Mun",
      "lgname_np": "जनकनन्दिनी गाउँपालिका",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 17,
        "did": 203,
        
        "district_en": "Dhanusha",
        "district_np": "धनुषा"
      }
    },
    {
      "id": 185,
      "lgid": 20313,
      
      "lgname_en": "Bideha Municipality",
      "lgname_np": "विदेह नगरपालिका",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 17,
        "did": 203,
        
        "district_en": "Dhanusha",
        "district_np": "धनुषा"
      }
    },
    {
      "id": 186,
      "lgid": 20314,
      
      "lgname_en": "Aurahi Rural Mun",
      "lgname_np": "औरही गाउँपालिका",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 17,
        "did": 203,
        
        "district_en": "Dhanusha",
        "district_np": "धनुषा"
      }
    },
    {
      "id": 187,
      "lgid": 20315,
      
      "lgname_en": "Janakpurdham Sub-Metro",
      "lgname_np": "जनकपुरधाम उपमहानगरपालिका",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 17,
        "did": 203,
        
        "district_en": "Dhanusha",
        "district_np": "धनुषा"
      }
    },
    {
      "id": 188,
      "lgid": 20316,
      
      "lgname_en": "Dhanauji Rural Mun",
      "lgname_np": "धनौजी गाउँपालिका",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 17,
        "did": 203,
        
        "district_en": "Dhanusha",
        "district_np": "धनुषा"
      }
    },
    {
      "id": 189,
      "lgid": 20317,
      
      "lgname_en": "Nagrain Municipality",
      "lgname_np": "नगराइन नगरपालिका",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 17,
        "did": 203,
        
        "district_en": "Dhanusha",
        "district_np": "धनुषा"
      }
    },
    {
      "id": 190,
      "lgid": 20318,
      
      "lgname_en": "Mukhiyapattimusaharmiya Rural Mun",
      "lgname_np": "मुखियापट्टी मुसहरमिया गाउँपालिका ",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 17,
        "did": 203,
        
        "district_en": "Dhanusha",
        "district_np": "धनुषा"
      }
    },
    {
      "id": 191,
      "lgid": 20401,
      
      "lgname_en": "Bardibas Municipality",
      "lgname_np": "बर्दिबास नगरपालिका ",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 18,
        "did": 204,
        
        "district_en": "Mahottari",
        "district_np": "महोत्तरी"
      }
    },
    {
      "id": 192,
      "lgid": 20402,
      
      "lgname_en": "Gaushala Municipality",
      "lgname_np": "गौशाला नगरपालिका ",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 18,
        "did": 204,
        
        "district_en": "Mahottari",
        "district_np": "महोत्तरी"
      }
    },
    {
      "id": 193,
      "lgid": 20403,
      
      "lgname_en": "Sonma Rural Mun",
      "lgname_np": "सोनमा गाउँपालिका ",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 18,
        "did": 204,
        
        "district_en": "Mahottari",
        "district_np": "महोत्तरी"
      }
    },
    {
      "id": 194,
      "lgid": 20404,
      
      "lgname_en": "Aurahi Municipality",
      "lgname_np": "औरही नगरपालिका ",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 18,
        "did": 204,
        
        "district_en": "Mahottari",
        "district_np": "महोत्तरी"
      }
    },
    {
      "id": 195,
      "lgid": 20405,
      
      "lgname_en": "Bhagaha Municipality",
      "lgname_np": "भँगाहा नगरपालिका ",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 18,
        "did": 204,
        
        "district_en": "Mahottari",
        "district_np": "महोत्तरी"
      }
    },
    {
      "id": 196,
      "lgid": 20406,
      
      "lgname_en": "Loharpatti Municipality",
      "lgname_np": "लोहरपट्टी नगरपालिका ",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 18,
        "did": 204,
        
        "district_en": "Mahottari",
        "district_np": "महोत्तरी"
      }
    },
    {
      "id": 197,
      "lgid": 20407,
      
      "lgname_en": "Balwa Municipality",
      "lgname_np": "बलवा नगरपालिका ",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 18,
        "did": 204,
        
        "district_en": "Mahottari",
        "district_np": "महोत्तरी"
      }
    },
    {
      "id": 198,
      "lgid": 20408,
      
      "lgname_en": "Ramgopalpur Municipality",
      "lgname_np": "रामगोपालपुर नगरपालिका ",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 18,
        "did": 204,
        
        "district_en": "Mahottari",
        "district_np": "महोत्तरी"
      }
    },
    {
      "id": 199,
      "lgid": 20409,
      
      "lgname_en": "Samsi Rural Mun",
      "lgname_np": "साम्सी गाउँपालिका ",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 18,
        "did": 204,
        
        "district_en": "Mahottari",
        "district_np": "महोत्तरी"
      }
    },
    {
      "id": 200,
      "lgid": 20410,
      
      "lgname_en": "Manrashiswa Municipality",
      "lgname_np": "मनरा शिसवा नगरपालिका ",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 18,
        "did": 204,
        
        "district_en": "Mahottari",
        "district_np": "महोत्तरी"
      }
    },
    {
      "id": 201,
      "lgid": 20411,
      
      "lgname_en": "Ekdara Rural Mun",
      "lgname_np": "एकडारा गाउँपालिका ",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 18,
        "did": 204,
        
        "district_en": "Mahottari",
        "district_np": "महोत्तरी"
      }
    },
    {
      "id": 202,
      "lgid": 20412,
      
      "lgname_en": "Mahottari Rural Mun",
      "lgname_np": "महोत्तरी गाउँपालिका ",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 18,
        "did": 204,
        
        "district_en": "Mahottari",
        "district_np": "महोत्तरी"
      }
    },
    {
      "id": 203,
      "lgid": 20413,
      
      "lgname_en": "Pipra Rural Mun",
      "lgname_np": "पिपरा गाउँपालिका ",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 18,
        "did": 204,
        
        "district_en": "Mahottari",
        "district_np": "महोत्तरी"
      }
    },
    {
      "id": 204,
      "lgid": 20414,
      
      "lgname_en": "Matihani Municipality",
      "lgname_np": "मटिहानी नगरपालिका ",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 18,
        "did": 204,
        
        "district_en": "Mahottari",
        "district_np": "महोत्तरी"
      }
    },
    {
      "id": 205,
      "lgid": 20415,
      
      "lgname_en": "Jaleshwor Municipality",
      "lgname_np": "जलेश्वर नगरपालिका ",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 18,
        "did": 204,
        
        "district_en": "Mahottari",
        "district_np": "महोत्तरी"
      }
    },
    {
      "id": 206,
      "lgid": 20501,
      
      "lgname_en": "Lalbandi Municipality",
      "lgname_np": "लालबन्दी नगरपालिका ",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 19,
        "did": 205,
        
        "district_en": "Sarlahi",
        "district_np": "सर्लाही"
      }
    },
    {
      "id": 207,
      "lgid": 20502,
      
      "lgname_en": "Harion Municipality",
      "lgname_np": "हरिवन नगरपालिका ",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 19,
        "did": 205,
        
        "district_en": "Sarlahi",
        "district_np": "सर्लाही"
      }
    },
    {
      "id": 208,
      "lgid": 20503,
      
      "lgname_en": "Bagmati Municipality",
      "lgname_np": "बागमती नगरपालिका ",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 19,
        "did": 205,
        
        "district_en": "Sarlahi",
        "district_np": "सर्लाही"
      }
    },
    {
      "id": 209,
      "lgid": 20504,
      
      "lgname_en": "Barhathwa Municipality",
      "lgname_np": "बरहथवा नगरपालिका ",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 19,
        "did": 205,
        
        "district_en": "Sarlahi",
        "district_np": "सर्लाही"
      }
    },
    {
      "id": 210,
      "lgid": 20505,
      
      "lgname_en": "Haripur Municipality",
      "lgname_np": "हरिपुर नगरपालिका ",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 19,
        "did": 205,
        
        "district_en": "Sarlahi",
        "district_np": "सर्लाही"
      }
    },
    {
      "id": 211,
      "lgid": 20506,
      
      "lgname_en": "Ishworpur Municipality",
      "lgname_np": "ईश्वरपुर नगरपालिका ",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 19,
        "did": 205,
        
        "district_en": "Sarlahi",
        "district_np": "सर्लाही"
      }
    },
    {
      "id": 212,
      "lgid": 20507,
      
      "lgname_en": "Haripurwa Municipality",
      "lgname_np": "हरिपुर्वा नगरपालिका ",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 19,
        "did": 205,
        
        "district_en": "Sarlahi",
        "district_np": "सर्लाही"
      }
    },
    {
      "id": 213,
      "lgid": 20508,
      
      "lgname_en": "Parsa Rural Mun",
      "lgname_np": "पर्सा गाउँपालिका",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 19,
        "did": 205,
        
        "district_en": "Sarlahi",
        "district_np": "सर्लाही"
      }
    },
    {
      "id": 214,
      "lgid": 20509,
      
      "lgname_en": "Brahmapuri Rural Mun",
      "lgname_np": "ब्रह्मपुरी गाउँपालिका ",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 19,
        "did": 205,
        
        "district_en": "Sarlahi",
        "district_np": "सर्लाही"
      }
    },
    {
      "id": 215,
      "lgid": 20510,
      
      "lgname_en": "Chandranagar Rural Mun",
      "lgname_np": "चन्द्रनगर गाउँपालिका ",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 19,
        "did": 205,
        
        "district_en": "Sarlahi",
        "district_np": "सर्लाही"
      }
    },
    {
      "id": 216,
      "lgid": 20511,
      
      "lgname_en": "Kawilasi Municipality",
      "lgname_np": "कविलासी नगरपालिका ",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 19,
        "did": 205,
        
        "district_en": "Sarlahi",
        "district_np": "सर्लाही"
      }
    },
    {
      "id": 217,
      "lgid": 20512,
      
      "lgname_en": "Chakraghatta Rural Mun",
      "lgname_np": "चक्रघट्टा गाउँपालिका ",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 19,
        "did": 205,
        
        "district_en": "Sarlahi",
        "district_np": "सर्लाही"
      }
    },
    {
      "id": 218,
      "lgid": 20513,
      
      "lgname_en": "Basbariya Rural Mun",
      "lgname_np": "बसबरीया गाउँपालिका",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 19,
        "did": 205,
        
        "district_en": "Sarlahi",
        "district_np": "सर्लाही"
      }
    },
    {
      "id": 219,
      "lgid": 20514,
      
      "lgname_en": "Dhankaul Rural Mun",
      "lgname_np": "धनकौल गाउँपालिका ",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 19,
        "did": 205,
        
        "district_en": "Sarlahi",
        "district_np": "सर्लाही"
      }
    },
    {
      "id": 220,
      "lgid": 20515,
      
      "lgname_en": "Ramnagar Rural Mun",
      "lgname_np": "रामनगर गाउँपालिका ",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 19,
        "did": 205,
        
        "district_en": "Sarlahi",
        "district_np": "सर्लाही"
      }
    },
    {
      "id": 221,
      "lgid": 20516,
      
      "lgname_en": "Balra Municipality",
      "lgname_np": "बलरा नगरपालिका ",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 19,
        "did": 205,
        
        "district_en": "Sarlahi",
        "district_np": "सर्लाही"
      }
    },
    {
      "id": 222,
      "lgid": 20517,
      
      "lgname_en": "Godaita Municipality",
      "lgname_np": "गोडैटा नगरपालिका ",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 19,
        "did": 205,
        
        "district_en": "Sarlahi",
        "district_np": "सर्लाही"
      }
    },
    {
      "id": 223,
      "lgid": 20518,
      
      "lgname_en": "Bishnu Rural Mun",
      "lgname_np": "विष्णु गाउँपालिका ",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 19,
        "did": 205,
        
        "district_en": "Sarlahi",
        "district_np": "सर्लाही"
      }
    },
    {
      "id": 224,
      "lgid": 20519,
      
      "lgname_en": "Kaudena Rural Mun",
      "lgname_np": "कौडेना गाउँपालिका",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 19,
        "did": 205,
        
        "district_en": "Sarlahi",
        "district_np": "सर्लाही"
      }
    },
    {
      "id": 225,
      "lgid": 20520,
      
      "lgname_en": "Malangwa Municipality",
      "lgname_np": "मलंगवा नगरपालिका ",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 19,
        "did": 205,
        
        "district_en": "Sarlahi",
        "district_np": "सर्लाही"
      }
    },
    {
      "id": 226,
      "lgid": 20601,
      
      "lgname_en": "Chandrapur Municipality",
      "lgname_np": "चन्द्रपुर नगरपालिका ",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 20,
        "did": 206,
        
        "district_en": "Rautahat",
        "district_np": "रौतहट"
      }
    },
    {
      "id": 227,
      "lgid": 20602,
      
      "lgname_en": "Gujara Municipality",
      "lgname_np": "गुजरा नगरपालिका ",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 20,
        "did": 206,
        
        "district_en": "Rautahat",
        "district_np": "रौतहट"
      }
    },
    {
      "id": 228,
      "lgid": 20603,
      
      "lgname_en": "Phatuwabijaypur Municipality",
      "lgname_np": "फतुवाबिजयपुर नगरपालिका ",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 20,
        "did": 206,
        
        "district_en": "Rautahat",
        "district_np": "रौतहट"
      }
    },
    {
      "id": 229,
      "lgid": 20604,
      
      "lgname_en": "Katahariya Municipality",
      "lgname_np": "कटहरिया नगरपालिका ",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 20,
        "did": 206,
        
        "district_en": "Rautahat",
        "district_np": "रौतहट"
      }
    },
    {
      "id": 230,
      "lgid": 20605,
      
      "lgname_en": "Brindawan Municipality",
      "lgname_np": "बृन्दावन नगरपालिका ",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 20,
        "did": 206,
        
        "district_en": "Rautahat",
        "district_np": "रौतहट"
      }
    },
    {
      "id": 231,
      "lgid": 20606,
      
      "lgname_en": "Gadhimai Municipality",
      "lgname_np": "गढीमाई नगरपालिका ",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 20,
        "did": 206,
        
        "district_en": "Rautahat",
        "district_np": "रौतहट"
      }
    },
    {
      "id": 232,
      "lgid": 20607,
      
      "lgname_en": "Madhavnarayan Municipality",
      "lgname_np": "माधव नारायण नगरपालिका ",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 20,
        "did": 206,
        
        "district_en": "Rautahat",
        "district_np": "रौतहट"
      }
    },
    {
      "id": 233,
      "lgid": 20608,
      
      "lgname_en": "Garuda Municipality",
      "lgname_np": "गरुडा नगरपालिका",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 20,
        "did": 206,
        
        "district_en": "Rautahat",
        "district_np": "रौतहट"
      }
    },
    {
      "id": 234,
      "lgid": 20609,
      
      "lgname_en": "Dewahigonahi Municipality",
      "lgname_np": "देवाही गोनाही नगरपालिका ",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 20,
        "did": 206,
        
        "district_en": "Rautahat",
        "district_np": "रौतहट"
      }
    },
    {
      "id": 235,
      "lgid": 20610,
      
      "lgname_en": "Maulapur Municipality",
      "lgname_np": "मौलापुर नगरपालिका ",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 20,
        "did": 206,
        
        "district_en": "Rautahat",
        "district_np": "रौतहट"
      }
    },
    {
      "id": 236,
      "lgid": 20611,
      
      "lgname_en": "Baudhimai Municipality",
      "lgname_np": "बौधीमाई नगरपालिका ",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 20,
        "did": 206,
        
        "district_en": "Rautahat",
        "district_np": "रौतहट"
      }
    },
    {
      "id": 237,
      "lgid": 20612,
      
      "lgname_en": "Paroha Municipality",
      "lgname_np": "परोहा नगरपालिका ",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 20,
        "did": 206,
        
        "district_en": "Rautahat",
        "district_np": "रौतहट"
      }
    },
    {
      "id": 238,
      "lgid": 20613,
      
      "lgname_en": "Rajpur Municipality",
      "lgname_np": "राजपुर नगरपालिका ",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 20,
        "did": 206,
        
        "district_en": "Rautahat",
        "district_np": "रौतहट"
      }
    },
    {
      "id": 239,
      "lgid": 20614,
      
      "lgname_en": "Yamunamai Rural Mun",
      "lgname_np": "यमुनामाई गाउँपालिका",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 20,
        "did": 206,
        
        "district_en": "Rautahat",
        "district_np": "रौतहट"
      }
    },
    {
      "id": 240,
      "lgid": 20615,
      
      "lgname_en": "Durgabhagawati Rural Mun",
      "lgname_np": "दुर्गा भगवती गाउँपालिका ",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 20,
        "did": 206,
        
        "district_en": "Rautahat",
        "district_np": "रौतहट"
      }
    },
    {
      "id": 241,
      "lgid": 20616,
      
      "lgname_en": "Rajdevi Municipality",
      "lgname_np": "राजदेवी नगरपालिका",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 20,
        "did": 206,
        
        "district_en": "Rautahat",
        "district_np": "रौतहट"
      }
    },
    {
      "id": 242,
      "lgid": 20617,
      
      "lgname_en": "Gaur Municipality",
      "lgname_np": "गौर नगरपालिका ",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 20,
        "did": 206,
        
        "district_en": "Rautahat",
        "district_np": "रौतहट"
      }
    },
    {
      "id": 243,
      "lgid": 20618,
      
      "lgname_en": "Ishnath Municipality",
      "lgname_np": "ईशनाथ नगरपालिका ",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 20,
        "did": 206,
        
        "district_en": "Rautahat",
        "district_np": "रौतहट"
      }
    },
    {
      "id": 244,
      "lgid": 20701,
      
      "lgname_en": "Nijgadh Municipality",
      "lgname_np": "निजगढ नगरपालिका ",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 21,
        "did": 207,
        
        "district_en": "Bara",
        "district_np": "वारा"
      }
    },
    {
      "id": 245,
      "lgid": 20702,
      
      "lgname_en": "Kolhabi Municipality",
      "lgname_np": "कोल्हवी नगरपालिका ",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 21,
        "did": 207,
        
        "district_en": "Bara",
        "district_np": "वारा"
      }
    },
    {
      "id": 246,
      "lgid": 20703,
      
      "lgname_en": "Jeetpursimara Sub-Metro",
      "lgname_np": "जीतपुर सिमरा उपमहानगरपालिका ",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 21,
        "did": 207,
        
        "district_en": "Bara",
        "district_np": "वारा"
      }
    },
    {
      "id": 247,
      "lgid": 20704,
      
      "lgname_en": "Parwanipur Rural Mun",
      "lgname_np": "परवानीपुर गाउँपालिका ",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 21,
        "did": 207,
        
        "district_en": "Bara",
        "district_np": "वारा"
      }
    },
    {
      "id": 248,
      "lgid": 20705,
      
      "lgname_en": "Prasauni Rural Mun",
      "lgname_np": "प्रसौनी गाउँपालिका ",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 21,
        "did": 207,
        
        "district_en": "Bara",
        "district_np": "वारा"
      }
    },
    {
      "id": 249,
      "lgid": 20706,
      
      "lgname_en": "Bishrampur Rural Mun",
      "lgname_np": "विश्रामपुर गाउँपालिका",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 21,
        "did": 207,
        
        "district_en": "Bara",
        "district_np": "वारा"
      }
    },
    {
      "id": 250,
      "lgid": 20707,
      
      "lgname_en": "Pheta Rural Mun",
      "lgname_np": "फेटा गाउँपालिका ",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 21,
        "did": 207,
        
        "district_en": "Bara",
        "district_np": "वारा"
      }
    },
    {
      "id": 251,
      "lgid": 20708,
      
      "lgname_en": "Kalaiya Sub-Metro",
      "lgname_np": "कलैया उपमहानगरपालिका ",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 21,
        "did": 207,
        
        "district_en": "Bara",
        "district_np": "वारा"
      }
    },
    {
      "id": 252,
      "lgid": 20709,
      
      "lgname_en": "Karaiyamai Rural Mun",
      "lgname_np": "करैयामाई गाउँपालिका ",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 21,
        "did": 207,
        
        "district_en": "Bara",
        "district_np": "वारा"
      }
    },
    {
      "id": 253,
      "lgid": 20710,
      
      "lgname_en": "Baragadhi Rural Mun",
      "lgname_np": "बारागढीगाउँपालिका ",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 21,
        "did": 207,
        
        "district_en": "Bara",
        "district_np": "वारा"
      }
    },
    {
      "id": 254,
      "lgid": 20711,
      
      "lgname_en": "Aadarshakotwal Rural Mun",
      "lgname_np": "आदर्श कोटवाल गाउँपालिका ",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 21,
        "did": 207,
        
        "district_en": "Bara",
        "district_np": "वारा"
      }
    },
    {
      "id": 255,
      "lgid": 20712,
      
      "lgname_en": "Simraungadh Municipality",
      "lgname_np": "सिम्रौनगढ नगरपालिका ",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 21,
        "did": 207,
        
        "district_en": "Bara",
        "district_np": "वारा"
      }
    },
    {
      "id": 256,
      "lgid": 20713,
      
      "lgname_en": "Pachrauta Municipality",
      "lgname_np": "पचरौता नगरपालिका ",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 21,
        "did": 207,
        
        "district_en": "Bara",
        "district_np": "वारा"
      }
    },
    {
      "id": 257,
      "lgid": 20714,
      
      "lgname_en": "Mahagadhimai Municipality",
      "lgname_np": "महागढीमाई नगरपालिका ",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 21,
        "did": 207,
        
        "district_en": "Bara",
        "district_np": "वारा"
      }
    },
    {
      "id": 258,
      "lgid": 20715,
      
      "lgname_en": "Devtal Rural Mun",
      "lgname_np": "देवताल गाउँपालिका ",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 21,
        "did": 207,
        
        "district_en": "Bara",
        "district_np": "वारा"
      }
    },
    {
      "id": 259,
      "lgid": 20716,
      
      "lgname_en": "Suwarna Rural Mun",
      "lgname_np": "सुवर्ण गाउँपालिका ",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 21,
        "did": 207,
        
        "district_en": "Bara",
        "district_np": "वारा"
      }
    },
    {
      "id": 260,
      "lgid": 20801,
      
      "lgname_en": "Thori Rural Mun",
      "lgname_np": "ठोरी गाउँपालिका ",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 22,
        "did": 208,
        
        "district_en": "Parsa",
        "district_np": "पर्सा"
      }
    },
    {
      "id": 261,
      "lgid": 20802,
      
      "lgname_en": "Jirabhawani Rural Mun",
      "lgname_np": "जिरा भवानी गाउँपालिका",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 22,
        "did": 208,
        
        "district_en": "Parsa",
        "district_np": "पर्सा"
      }
    },
    {
      "id": 262,
      "lgid": 20803,
      
      "lgname_en": "Jagarnathpur Rural Mun",
      "lgname_np": "जगरनाथपुर गाउँपालिका ",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 22,
        "did": 208,
        
        "district_en": "Parsa",
        "district_np": "पर्सा"
      }
    },
    {
      "id": 263,
      "lgid": 20804,
      
      "lgname_en": "Paterwasugauli Rural Mun",
      "lgname_np": "पटेर्वा सुगौली गाउँपालिका ",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 22,
        "did": 208,
        
        "district_en": "Parsa",
        "district_np": "पर्सा"
      }
    },
    {
      "id": 264,
      "lgid": 20805,
      
      "lgname_en": "Sakhuwaprasauni Rural Mun",
      "lgname_np": "सखुवा प्रसौनी गाउँपालिका ",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 22,
        "did": 208,
        
        "district_en": "Parsa",
        "district_np": "पर्सा"
      }
    },
    {
      "id": 265,
      "lgid": 20806,
      
      "lgname_en": "Parsagadhi Municipality",
      "lgname_np": "पर्सागढी नगरपालिका ",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 22,
        "did": 208,
        
        "district_en": "Parsa",
        "district_np": "पर्सा"
      }
    },
    {
      "id": 266,
      "lgid": 20807,
      
      "lgname_en": "Birgunj Metro",
      "lgname_np": "बिरगंज महानगरपालिका",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 22,
        "did": 208,
        
        "district_en": "Parsa",
        "district_np": "पर्सा"
      }
    },
    {
      "id": 267,
      "lgid": 20808,
      
      "lgname_en": "Bahudarmai Municipality",
      "lgname_np": "बहुदरमाई नगरपालिका ",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 22,
        "did": 208,
        
        "district_en": "Parsa",
        "district_np": "पर्सा"
      }
    },
    {
      "id": 268,
      "lgid": 20809,
      
      "lgname_en": "Pokhariya Municipality",
      "lgname_np": "पोखरिया नगरपालिका ",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 22,
        "did": 208,
        
        "district_en": "Parsa",
        "district_np": "पर्सा"
      }
    },
    {
      "id": 269,
      "lgid": 20810,
      
      "lgname_en": "Kalikamai Rural Mun",
      "lgname_np": "कालिकामाई गाउँपालिका",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 22,
        "did": 208,
        
        "district_en": "Parsa",
        "district_np": "पर्सा"
      }
    },
    {
      "id": 270,
      "lgid": 20811,
      
      "lgname_en": "Dhobini Rural Mun",
      "lgname_np": "धोबीनी गाउँपालिका ",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 22,
        "did": 208,
        
        "district_en": "Parsa",
        "district_np": "पर्सा"
      }
    },
    {
      "id": 271,
      "lgid": 20812,
      
      "lgname_en": "Chhipaharmai Rural Mun",
      "lgname_np": "छिपहरमाई गाउँपालिका",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 22,
        "did": 208,
        
        "district_en": "Parsa",
        "district_np": "पर्सा"
      }
    },
    {
      "id": 272,
      "lgid": 20813,
      
      "lgname_en": "Pakahamainpur Rural Mun",
      "lgname_np": "पकाहा मैनपुर गाउँपालिका ",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 22,
        "did": 208,
        
        "district_en": "Parsa",
        "district_np": "पर्सा"
      }
    },
    {
      "id": 273,
      "lgid": 20814,
      
      "lgname_en": "Bindabasini Rural Mun",
      "lgname_np": "बिन्दबासिनी गाउँपालिका",
      "province": {
        "id": 2,
        "province_en": "Madesh Province",
        "province_np": "मधेश प्रदेश",
        
      },
      "district": {
        "id": 22,
        "did": 208,
        
        "district_en": "Parsa",
        "district_np": "पर्सा"
      }
    },
    {
      "id": 274,
      "lgid": 30101,
      
      "lgname_en": "Gaurishankar Rural Mun",
      "lgname_np": "गौरीशङ्कर गाउँपालिका",
      "province": {
        "id": 3,
        "province_en": "Bagmati Province",
        "province_np": "बाग्मती प्रदेश",
        
      },
      "district": {
        "id": 23,
        "did": 301,
        
        "district_en": "Dolakha",
        "district_np": "दोलखा"
      }
    },
    {
      "id": 275,
      "lgid": 30102,
      
      "lgname_en": "Bigu Rural Mun",
      "lgname_np": "विगु गाउँपालिका",
      "province": {
        "id": 3,
        "province_en": "Bagmati Province",
        "province_np": "बाग्मती प्रदेश",
        
      },
      "district": {
        "id": 23,
        "did": 301,
        
        "district_en": "Dolakha",
        "district_np": "दोलखा"
      }
    },
    {
      "id": 276,
      "lgid": 30103,
      
      "lgname_en": "Kalinchowk Rural Mun",
      "lgname_np": "कालिन्चोक गाउँपालिका",
      "province": {
        "id": 3,
        "province_en": "Bagmati Province",
        "province_np": "बाग्मती प्रदेश",
        
      },
      "district": {
        "id": 23,
        "did": 301,
        
        "district_en": "Dolakha",
        "district_np": "दोलखा"
      }
    },
    {
      "id": 277,
      "lgid": 30104,
      
      "lgname_en": "Baiteshwor Rural Mun",
      "lgname_np": "वैतेश्वर गाउँपालिका",
      "province": {
        "id": 3,
        "province_en": "Bagmati Province",
        "province_np": "बाग्मती प्रदेश",
        
      },
      "district": {
        "id": 23,
        "did": 301,
        
        "district_en": "Dolakha",
        "district_np": "दोलखा"
      }
    },
    {
      "id": 278,
      "lgid": 30105,
      
      "lgname_en": "Jiri Municipality",
      "lgname_np": "जिरी नगरपालिका",
      "province": {
        "id": 3,
        "province_en": "Bagmati Province",
        "province_np": "बाग्मती प्रदेश",
        
      },
      "district": {
        "id": 23,
        "did": 301,
        
        "district_en": "Dolakha",
        "district_np": "दोलखा"
      }
    },
    {
      "id": 279,
      "lgid": 30106,
      
      "lgname_en": "Tamakoshi Rural Mun",
      "lgname_np": "तामाकोशी गाउँपालिका",
      "province": {
        "id": 3,
        "province_en": "Bagmati Province",
        "province_np": "बाग्मती प्रदेश",
        
      },
      "district": {
        "id": 23,
        "did": 301,
        
        "district_en": "Dolakha",
        "district_np": "दोलखा"
      }
    },
    {
      "id": 280,
      "lgid": 30107,
      
      "lgname_en": "Melung Rural Mun",
      "lgname_np": "मेलुङ्ग गाउँपालिका",
      "province": {
        "id": 3,
        "province_en": "Bagmati Province",
        "province_np": "बाग्मती प्रदेश",
        
      },
      "district": {
        "id": 23,
        "did": 301,
        
        "district_en": "Dolakha",
        "district_np": "दोलखा"
      }
    },
    {
      "id": 281,
      "lgid": 30108,
      
      "lgname_en": "Shailung Rural Mun",
      "lgname_np": "शैलुङ्ग गाउँपालिका",
      "province": {
        "id": 3,
        "province_en": "Bagmati Province",
        "province_np": "बाग्मती प्रदेश",
        
      },
      "district": {
        "id": 23,
        "did": 301,
        
        "district_en": "Dolakha",
        "district_np": "दोलखा"
      }
    },
    {
      "id": 282,
      "lgid": 30109,
      
      "lgname_en": "Bhimeshwor Municipality",
      "lgname_np": "भिमेश्वर नगरपालिका",
      "province": {
        "id": 3,
        "province_en": "Bagmati Province",
        "province_np": "बाग्मती प्रदेश",
        
      },
      "district": {
        "id": 23,
        "did": 301,
        
        "district_en": "Dolakha",
        "district_np": "दोलखा"
      }
    },
    {
      "id": 283,
      "lgid": 30201,
      
      "lgname_en": "Bhotekoshi Rural Mun",
      "lgname_np": "भोटेकोशी गाउँपालिका",
      "province": {
        "id": 3,
        "province_en": "Bagmati Province",
        "province_np": "बाग्मती प्रदेश",
        
      },
      "district": {
        "id": 24,
        "did": 302,
        
        "district_en": "Sindhupalchowk",
        "district_np": "सिन्धुपाल्चोक"
      }
    },
    {
      "id": 284,
      "lgid": 30202,
      
      "lgname_en": "Jugal Rural Mun",
      "lgname_np": "जुगल गाउँपालिका",
      "province": {
        "id": 3,
        "province_en": "Bagmati Province",
        "province_np": "बाग्मती प्रदेश",
        
      },
      "district": {
        "id": 24,
        "did": 302,
        
        "district_en": "Sindhupalchowk",
        "district_np": "सिन्धुपाल्चोक"
      }
    },
    {
      "id": 285,
      "lgid": 30203,
      
      "lgname_en": "Panchpokharithangpal Rural Mun",
      "lgname_np": "पाँचपोखरी थाङपाल गाउँपालिका",
      "province": {
        "id": 3,
        "province_en": "Bagmati Province",
        "province_np": "बाग्मती प्रदेश",
        
      },
      "district": {
        "id": 24,
        "did": 302,
        
        "district_en": "Sindhupalchowk",
        "district_np": "सिन्धुपाल्चोक"
      }
    },
    {
      "id": 286,
      "lgid": 30204,
      
      "lgname_en": "Helambu Rural Mun",
      "lgname_np": "हेलम्बु गाउँपालिका",
      "province": {
        "id": 3,
        "province_en": "Bagmati Province",
        "province_np": "बाग्मती प्रदेश",
        
      },
      "district": {
        "id": 24,
        "did": 302,
        
        "district_en": "Sindhupalchowk",
        "district_np": "सिन्धुपाल्चोक"
      }
    },
    {
      "id": 287,
      "lgid": 30205,
      
      "lgname_en": "Melamchi Municipality",
      "lgname_np": "मेलम्ची नगरपालिका",
      "province": {
        "id": 3,
        "province_en": "Bagmati Province",
        "province_np": "बाग्मती प्रदेश",
        
      },
      "district": {
        "id": 24,
        "did": 302,
        
        "district_en": "Sindhupalchowk",
        "district_np": "सिन्धुपाल्चोक"
      }
    },
    {
      "id": 288,
      "lgid": 30206,
      
      "lgname_en": "Indrawati Rural Mun",
      "lgname_np": "ईन्द्रावती गाउँपालिका",
      "province": {
        "id": 3,
        "province_en": "Bagmati Province",
        "province_np": "बाग्मती प्रदेश",
        
      },
      "district": {
        "id": 24,
        "did": 302,
        
        "district_en": "Sindhupalchowk",
        "district_np": "सिन्धुपाल्चोक"
      }
    },
    {
      "id": 289,
      "lgid": 30207,
      
      "lgname_en": "Chautarasangachowkgadhi Municipality",
      "lgname_np": "चौतारा साँगाचोकगढी नगरपालिका",
      "province": {
        "id": 3,
        "province_en": "Bagmati Province",
        "province_np": "बाग्मती प्रदेश",
        
      },
      "district": {
        "id": 24,
        "did": 302,
        
        "district_en": "Sindhupalchowk",
        "district_np": "सिन्धुपाल्चोक"
      }
    },
    {
      "id": 290,
      "lgid": 30208,
      
      "lgname_en": "Balephi Rural Mun",
      "lgname_np": "बलेफी गाउँपालिका",
      "province": {
        "id": 3,
        "province_en": "Bagmati Province",
        "province_np": "बाग्मती प्रदेश",
        
      },
      "district": {
        "id": 24,
        "did": 302,
        
        "district_en": "Sindhupalchowk",
        "district_np": "सिन्धुपाल्चोक"
      }
    },
    {
      "id": 291,
      "lgid": 30209,
      
      "lgname_en": "Bahrabise Municipality",
      "lgname_np": "बाह्रविसे नगरपालिका",
      "province": {
        "id": 3,
        "province_en": "Bagmati Province",
        "province_np": "बाग्मती प्रदेश",
        
      },
      "district": {
        "id": 24,
        "did": 302,
        
        "district_en": "Sindhupalchowk",
        "district_np": "सिन्धुपाल्चोक"
      }
    },
    {
      "id": 292,
      "lgid": 30210,
      
      "lgname_en": "Tripurasundari Rural Mun",
      "lgname_np": "त्रिपुरासुन्दरी गाउँपालिका",
      "province": {
        "id": 3,
        "province_en": "Bagmati Province",
        "province_np": "बाग्मती प्रदेश",
        
      },
      "district": {
        "id": 24,
        "did": 302,
        
        "district_en": "Sindhupalchowk",
        "district_np": "सिन्धुपाल्चोक"
      }
    },
    {
      "id": 293,
      "lgid": 30211,
      
      "lgname_en": "Lisankhupakhar Rural Mun",
      "lgname_np": "लिसङ्खु पाखर गाउँपालिका",
      "province": {
        "id": 3,
        "province_en": "Bagmati Province",
        "province_np": "बाग्मती प्रदेश",
        
      },
      "district": {
        "id": 24,
        "did": 302,
        
        "district_en": "Sindhupalchowk",
        "district_np": "सिन्धुपाल्चोक"
      }
    },
    {
      "id": 294,
      "lgid": 30212,
      
      "lgname_en": "Sunkoshi Rural Mun",
      "lgname_np": "सुनकोशी गाउँपालिका",
      "province": {
        "id": 3,
        "province_en": "Bagmati Province",
        "province_np": "बाग्मती प्रदेश",
        
      },
      "district": {
        "id": 24,
        "did": 302,
        
        "district_en": "Sindhupalchowk",
        "district_np": "सिन्धुपाल्चोक"
      }
    },
    {
      "id": 295,
      "lgid": 30301,
      
      "lgname_en": "Gosaikunda Rural Mun",
      "lgname_np": "गोसाईकुण्ड गाउँपालिका",
      "province": {
        "id": 3,
        "province_en": "Bagmati Province",
        "province_np": "बाग्मती प्रदेश",
        
      },
      "district": {
        "id": 25,
        "did": 303,
        
        "district_en": "Rasuwa",
        "district_np": "रसुवा"
      }
    },
    {
      "id": 296,
      "lgid": 30302,
      
      "lgname_en": "Aamachhodingmo Rural Mun",
      "lgname_np": "आमाछोदिङमो गाउँपालिका",
      "province": {
        "id": 3,
        "province_en": "Bagmati Province",
        "province_np": "बाग्मती प्रदेश",
        
      },
      "district": {
        "id": 25,
        "did": 303,
        
        "district_en": "Rasuwa",
        "district_np": "रसुवा"
      }
    },
    {
      "id": 297,
      "lgid": 30303,
      
      "lgname_en": "Uttargaya Rural Mun",
      "lgname_np": "उत्तरगया गाउँपालिका",
      "province": {
        "id": 3,
        "province_en": "Bagmati Province",
        "province_np": "बाग्मती प्रदेश",
        
      },
      "district": {
        "id": 25,
        "did": 303,
        
        "district_en": "Rasuwa",
        "district_np": "रसुवा"
      }
    },
    {
      "id": 298,
      "lgid": 30304,
      
      "lgname_en": "Kalika Rural Mun",
      "lgname_np": "कालिका गाउँपालिका",
      "province": {
        "id": 3,
        "province_en": "Bagmati Province",
        "province_np": "बाग्मती प्रदेश",
        
      },
      "district": {
        "id": 25,
        "did": 303,
        
        "district_en": "Rasuwa",
        "district_np": "रसुवा"
      }
    },
    {
      "id": 299,
      "lgid": 30305,
      
      "lgname_en": "Naukunda Rural Mun",
      "lgname_np": "नौकुण्ड गाउँपालिका",
      "province": {
        "id": 3,
        "province_en": "Bagmati Province",
        "province_np": "बाग्मती प्रदेश",
        
      },
      "district": {
        "id": 25,
        "did": 303,
        
        "district_en": "Rasuwa",
        "district_np": "रसुवा"
      }
    },
    {
      "id": 300,
      "lgid": 30401,
      
      "lgname_en": "Rubivalley Rural Mun",
      "lgname_np": "रुवी भ्याली गाउँपालिका",
      "province": {
        "id": 3,
        "province_en": "Bagmati Province",
        "province_np": "बाग्मती प्रदेश",
        
      },
      "district": {
        "id": 26,
        "did": 304,
        
        "district_en": "Dhading",
        "district_np": "धादिङ"
      }
    },
    {
      "id": 301,
      "lgid": 30402,
      
      "lgname_en": "Khaniyabas Rural Mun",
      "lgname_np": "खनियाबास गाउँपालिका",
      "province": {
        "id": 3,
        "province_en": "Bagmati Province",
        "province_np": "बाग्मती प्रदेश",
        
      },
      "district": {
        "id": 26,
        "did": 304,
        
        "district_en": "Dhading",
        "district_np": "धादिङ"
      }
    },
    {
      "id": 302,
      "lgid": 30403,
      
      "lgname_en": "Gangajamuna Rural Mun",
      "lgname_np": "गङ्गाजमुना गाउँपालिका",
      "province": {
        "id": 3,
        "province_en": "Bagmati Province",
        "province_np": "बाग्मती प्रदेश",
        
      },
      "district": {
        "id": 26,
        "did": 304,
        
        "district_en": "Dhading",
        "district_np": "धादिङ"
      }
    },
    {
      "id": 303,
      "lgid": 30404,
      
      "lgname_en": "Tripurasundari Rural Mun",
      "lgname_np": "त्रिपुरासुन्दरी गाउँपालिका",
      "province": {
        "id": 3,
        "province_en": "Bagmati Province",
        "province_np": "बाग्मती प्रदेश",
        
      },
      "district": {
        "id": 26,
        "did": 304,
        
        "district_en": "Dhading",
        "district_np": "धादिङ"
      }
    },
    {
      "id": 304,
      "lgid": 30405,
      
      "lgname_en": "Netrawati Dabjong Rural Mun",
      "lgname_np": "नेत्रावती डबजोङ गाउँपालिका",
      "province": {
        "id": 3,
        "province_en": "Bagmati Province",
        "province_np": "बाग्मती प्रदेश",
        
      },
      "district": {
        "id": 26,
        "did": 304,
        
        "district_en": "Dhading",
        "district_np": "धादिङ"
      }
    },
    {
      "id": 305,
      "lgid": 30406,
      
      "lgname_en": "Neelakantha Municipality",
      "lgname_np": "निलकण्ठ नगरपालिका",
      "province": {
        "id": 3,
        "province_en": "Bagmati Province",
        "province_np": "बाग्मती प्रदेश",
        
      },
      "district": {
        "id": 26,
        "did": 304,
        
        "district_en": "Dhading",
        "district_np": "धादिङ"
      }
    },
    {
      "id": 306,
      "lgid": 30407,
      
      "lgname_en": "Jwalamukhi Rural Mun",
      "lgname_np": "ज्वालामूखी गाउँपालिका",
      "province": {
        "id": 3,
        "province_en": "Bagmati Province",
        "province_np": "बाग्मती प्रदेश",
        
      },
      "district": {
        "id": 26,
        "did": 304,
        
        "district_en": "Dhading",
        "district_np": "धादिङ"
      }
    },
    {
      "id": 307,
      "lgid": 30408,
      
      "lgname_en": "Siddhalek Rural Mun",
      "lgname_np": "सिद्धलेक गाउँपालिका",
      "province": {
        "id": 3,
        "province_en": "Bagmati Province",
        "province_np": "बाग्मती प्रदेश",
        
      },
      "district": {
        "id": 26,
        "did": 304,
        
        "district_en": "Dhading",
        "district_np": "धादिङ"
      }
    },
    {
      "id": 308,
      "lgid": 30409,
      
      "lgname_en": "Benighatrorang Rural Mun",
      "lgname_np": "बेनीघाट रोराङ्ग गाउँपालिका",
      "province": {
        "id": 3,
        "province_en": "Bagmati Province",
        "province_np": "बाग्मती प्रदेश",
        
      },
      "district": {
        "id": 26,
        "did": 304,
        
        "district_en": "Dhading",
        "district_np": "धादिङ"
      }
    },
    {
      "id": 309,
      "lgid": 30410,
      
      "lgname_en": "Gajuri Rural Mun",
      "lgname_np": "गजुरी गाउँपालिका",
      "province": {
        "id": 3,
        "province_en": "Bagmati Province",
        "province_np": "बाग्मती प्रदेश",
        
      },
      "district": {
        "id": 26,
        "did": 304,
        
        "district_en": "Dhading",
        "district_np": "धादिङ"
      }
    },
    {
      "id": 310,
      "lgid": 30411,
      
      "lgname_en": "Galchhi Rural Mun",
      "lgname_np": "गल्छी गाउँपालिका",
      "province": {
        "id": 3,
        "province_en": "Bagmati Province",
        "province_np": "बाग्मती प्रदेश",
        
      },
      "district": {
        "id": 26,
        "did": 304,
        
        "district_en": "Dhading",
        "district_np": "धादिङ"
      }
    },
    {
      "id": 311,
      "lgid": 30412,
      
      "lgname_en": "Thakre Rural Mun",
      "lgname_np": "थाक्रे गाउँपालिका",
      "province": {
        "id": 3,
        "province_en": "Bagmati Province",
        "province_np": "बाग्मती प्रदेश",
        
      },
      "district": {
        "id": 26,
        "did": 304,
        
        "district_en": "Dhading",
        "district_np": "धादिङ"
      }
    },
    {
      "id": 312,
      "lgid": 30413,
      
      "lgname_en": "Dhunibeshi Municipality",
      "lgname_np": "धुनीबेंशी नगरपालिका",
      "province": {
        "id": 3,
        "province_en": "Bagmati Province",
        "province_np": "बाग्मती प्रदेश",
        
      },
      "district": {
        "id": 26,
        "did": 304,
        
        "district_en": "Dhading",
        "district_np": "धादिङ"
      }
    },
    {
      "id": 313,
      "lgid": 30501,
      
      "lgname_en": "Dupcheshwor Rural Mun",
      "lgname_np": "दुप्चेश्वर गाउँपालिका",
      "province": {
        "id": 3,
        "province_en": "Bagmati Province",
        "province_np": "बाग्मती प्रदेश",
        
      },
      "district": {
        "id": 27,
        "did": 305,
        
        "district_en": "Nuwakot",
        "district_np": "नुवाकोट"
      }
    },
    {
      "id": 314,
      "lgid": 30502,
      
      "lgname_en": "Tadi Rural Mun",
      "lgname_np": "तादी गाउँपालिका",
      "province": {
        "id": 3,
        "province_en": "Bagmati Province",
        "province_np": "बाग्मती प्रदेश",
        
      },
      "district": {
        "id": 27,
        "did": 305,
        
        "district_en": "Nuwakot",
        "district_np": "नुवाकोट"
      }
    },
    {
      "id": 315,
      "lgid": 30503,
      
      "lgname_en": "Suryagadhi Rural Mun",
      "lgname_np": "सुर्यगढी गाउँपालिका",
      "province": {
        "id": 3,
        "province_en": "Bagmati Province",
        "province_np": "बाग्मती प्रदेश",
        
      },
      "district": {
        "id": 27,
        "did": 305,
        
        "district_en": "Nuwakot",
        "district_np": "नुवाकोट"
      }
    },
    {
      "id": 316,
      "lgid": 30504,
      
      "lgname_en": "Bidur Municipality",
      "lgname_np": "विदुर नगरपालिका",
      "province": {
        "id": 3,
        "province_en": "Bagmati Province",
        "province_np": "बाग्मती प्रदेश",
        
      },
      "district": {
        "id": 27,
        "did": 305,
        
        "district_en": "Nuwakot",
        "district_np": "नुवाकोट"
      }
    },
    {
      "id": 317,
      "lgid": 30505,
      
      "lgname_en": "Kispang Rural Mun",
      "lgname_np": "किस्पाङ गाउँपालिका",
      "province": {
        "id": 3,
        "province_en": "Bagmati Province",
        "province_np": "बाग्मती प्रदेश",
        
      },
      "district": {
        "id": 27,
        "did": 305,
        
        "district_en": "Nuwakot",
        "district_np": "नुवाकोट"
      }
    },
    {
      "id": 318,
      "lgid": 30506,
      
      "lgname_en": "Myagang Rural Mun",
      "lgname_np": "म्यगङ गाउँपालिका",
      "province": {
        "id": 3,
        "province_en": "Bagmati Province",
        "province_np": "बाग्मती प्रदेश",
        
      },
      "district": {
        "id": 27,
        "did": 305,
        
        "district_en": "Nuwakot",
        "district_np": "नुवाकोट"
      }
    },
    {
      "id": 319,
      "lgid": 30507,
      
      "lgname_en": "Tarakeshwor Rural Mun",
      "lgname_np": "तारकेश्वर गाउँपालिका",
      "province": {
        "id": 3,
        "province_en": "Bagmati Province",
        "province_np": "बाग्मती प्रदेश",
        
      },
      "district": {
        "id": 27,
        "did": 305,
        
        "district_en": "Nuwakot",
        "district_np": "नुवाकोट"
      }
    },
    {
      "id": 320,
      "lgid": 30508,
      
      "lgname_en": "Belkotgadhi Municipality",
      "lgname_np": "बेलकोटगढी नगरपालिका",
      "province": {
        "id": 3,
        "province_en": "Bagmati Province",
        "province_np": "बाग्मती प्रदेश",
        
      },
      "district": {
        "id": 27,
        "did": 305,
        
        "district_en": "Nuwakot",
        "district_np": "नुवाकोट"
      }
    },
    {
      "id": 321,
      "lgid": 30509,
      
      "lgname_en": "Likhu Rural Mun",
      "lgname_np": "लिखु गाउँपालिका",
      "province": {
        "id": 3,
        "province_en": "Bagmati Province",
        "province_np": "बाग्मती प्रदेश",
        
      },
      "district": {
        "id": 27,
        "did": 305,
        
        "district_en": "Nuwakot",
        "district_np": "नुवाकोट"
      }
    },
    {
      "id": 322,
      "lgid": 30510,
      
      "lgname_en": "Panchakanya Rural Mun",
      "lgname_np": "पञ्चकन्या गाउँपालिका",
      "province": {
        "id": 3,
        "province_en": "Bagmati Province",
        "province_np": "बाग्मती प्रदेश",
        
      },
      "district": {
        "id": 27,
        "did": 305,
        
        "district_en": "Nuwakot",
        "district_np": "नुवाकोट"
      }
    },
    {
      "id": 323,
      "lgid": 30511,
      
      "lgname_en": "Shivapuri Rural Mun",
      "lgname_np": "शिवपुरी गाउँपालिका",
      "province": {
        "id": 3,
        "province_en": "Bagmati Province",
        "province_np": "बाग्मती प्रदेश",
        
      },
      "district": {
        "id": 27,
        "did": 305,
        
        "district_en": "Nuwakot",
        "district_np": "नुवाकोट"
      }
    },
    {
      "id": 324,
      "lgid": 30512,
      
      "lgname_en": "Kakani Rural Mun",
      "lgname_np": "ककनी गाउँपालिका",
      "province": {
        "id": 3,
        "province_en": "Bagmati Province",
        "province_np": "बाग्मती प्रदेश",
        
      },
      "district": {
        "id": 27,
        "did": 305,
        
        "district_en": "Nuwakot",
        "district_np": "नुवाकोट"
      }
    },
    {
      "id": 325,
      "lgid": 30601,
      
      "lgname_en": "Shankharapur Municipality",
      "lgname_np": "शङ्खरापुर नगरपालिका",
      "province": {
        "id": 3,
        "province_en": "Bagmati Province",
        "province_np": "बाग्मती प्रदेश",
        
      },
      "district": {
        "id": 28,
        "did": 306,
        
        "district_en": "Kathmandu",
        "district_np": "काठमाण्डौ"
      }
    },
    {
      "id": 326,
      "lgid": 30602,
      
      "lgname_en": "Kageshworimanohara Municipality",
      "lgname_np": "कागेश्वरी मनोहरा नगरपालिका",
      "province": {
        "id": 3,
        "province_en": "Bagmati Province",
        "province_np": "बाग्मती प्रदेश",
        
      },
      "district": {
        "id": 28,
        "did": 306,
        
        "district_en": "Kathmandu",
        "district_np": "काठमाण्डौ"
      }
    },
    {
      "id": 327,
      "lgid": 30603,
      
      "lgname_en": "Gokarneshwor Municipality",
      "lgname_np": "गोकर्णेश्वर नगरपालिका",
      "province": {
        "id": 3,
        "province_en": "Bagmati Province",
        "province_np": "बाग्मती प्रदेश",
        
      },
      "district": {
        "id": 28,
        "did": 306,
        
        "district_en": "Kathmandu",
        "district_np": "काठमाण्डौ"
      }
    },
    {
      "id": 328,
      "lgid": 30604,
      
      "lgname_en": "Budhanilkantha Municipality",
      "lgname_np": "बुढानिलकण्ठ नगरपालिका",
      "province": {
        "id": 3,
        "province_en": "Bagmati Province",
        "province_np": "बाग्मती प्रदेश",
        
      },
      "district": {
        "id": 28,
        "did": 306,
        
        "district_en": "Kathmandu",
        "district_np": "काठमाण्डौ"
      }
    },
    {
      "id": 329,
      "lgid": 30605,
      
      "lgname_en": "Tokha Municipality",
      "lgname_np": "टोखा नगरपालिका",
      "province": {
        "id": 3,
        "province_en": "Bagmati Province",
        "province_np": "बाग्मती प्रदेश",
        
      },
      "district": {
        "id": 28,
        "did": 306,
        
        "district_en": "Kathmandu",
        "district_np": "काठमाण्डौ"
      }
    },
    {
      "id": 330,
      "lgid": 30606,
      
      "lgname_en": "Tarakeshwor Municipality",
      "lgname_np": "तारकेश्वर नगरपालिका",
      "province": {
        "id": 3,
        "province_en": "Bagmati Province",
        "province_np": "बाग्मती प्रदेश",
        
      },
      "district": {
        "id": 28,
        "did": 306,
        
        "district_en": "Kathmandu",
        "district_np": "काठमाण्डौ"
      }
    },
    {
      "id": 331,
      "lgid": 30607,
      
      "lgname_en": "Nagarjun Municipality",
      "lgname_np": "नागार्जुन नगरपालिका",
      "province": {
        "id": 3,
        "province_en": "Bagmati Province",
        "province_np": "बाग्मती प्रदेश",
        
      },
      "district": {
        "id": 28,
        "did": 306,
        
        "district_en": "Kathmandu",
        "district_np": "काठमाण्डौ"
      }
    },
    {
      "id": 332,
      "lgid": 30608,
      
      "lgname_en": "Kathmandu Metro",
      "lgname_np": "काठमाण्डौं महानगरपालिका",
      "province": {
        "id": 3,
        "province_en": "Bagmati Province",
        "province_np": "बाग्मती प्रदेश",
        
      },
      "district": {
        "id": 28,
        "did": 306,
        
        "district_en": "Kathmandu",
        "district_np": "काठमाण्डौ"
      }
    },
    {
      "id": 333,
      "lgid": 30609,
      
      "lgname_en": "Kirtipur Municipality",
      "lgname_np": "कीर्तिपुर नगरपालिका",
      "province": {
        "id": 3,
        "province_en": "Bagmati Province",
        "province_np": "बाग्मती प्रदेश",
        
      },
      "district": {
        "id": 28,
        "did": 306,
        
        "district_en": "Kathmandu",
        "district_np": "काठमाण्डौ"
      }
    },
    {
      "id": 334,
      "lgid": 30610,
      
      "lgname_en": "Chandragiri Municipality",
      "lgname_np": "चन्द्रागिरी नगरपालिका",
      "province": {
        "id": 3,
        "province_en": "Bagmati Province",
        "province_np": "बाग्मती प्रदेश",
        
      },
      "district": {
        "id": 28,
        "did": 306,
        
        "district_en": "Kathmandu",
        "district_np": "काठमाण्डौ"
      }
    },
    {
      "id": 335,
      "lgid": 30611,
      
      "lgname_en": "Dakshinkali Municipality",
      "lgname_np": "दक्षिणकाली नगरपालिका",
      "province": {
        "id": 3,
        "province_en": "Bagmati Province",
        "province_np": "बाग्मती प्रदेश",
        
      },
      "district": {
        "id": 28,
        "did": 306,
        
        "district_en": "Kathmandu",
        "district_np": "काठमाण्डौ"
      }
    },
    {
      "id": 336,
      "lgid": 30701,
      
      "lgname_en": "Changunarayan Municipality",
      "lgname_np": "चाँगुनारायण नगरपालिका",
      "province": {
        "id": 3,
        "province_en": "Bagmati Province",
        "province_np": "बाग्मती प्रदेश",
        
      },
      "district": {
        "id": 29,
        "did": 307,
        
        "district_en": "Bhaktapur",
        "district_np": "भक्तपुर"
      }
    },
    {
      "id": 337,
      "lgid": 30702,
      
      "lgname_en": "Bhaktapur Municipality",
      "lgname_np": "भक्तपुर नगरपालिका",
      "province": {
        "id": 3,
        "province_en": "Bagmati Province",
        "province_np": "बाग्मती प्रदेश",
        
      },
      "district": {
        "id": 29,
        "did": 307,
        
        "district_en": "Bhaktapur",
        "district_np": "भक्तपुर"
      }
    },
    {
      "id": 338,
      "lgid": 30703,
      
      "lgname_en": "Madhyapurthimi Municipality",
      "lgname_np": "मध्यपुर थिमी नगरपालिका",
      "province": {
        "id": 3,
        "province_en": "Bagmati Province",
        "province_np": "बाग्मती प्रदेश",
        
      },
      "district": {
        "id": 29,
        "did": 307,
        
        "district_en": "Bhaktapur",
        "district_np": "भक्तपुर"
      }
    },
    {
      "id": 339,
      "lgid": 30704,
      
      "lgname_en": "Suryabinayak Municipality",
      "lgname_np": "सूर्यविनायक नगरपालिका",
      "province": {
        "id": 3,
        "province_en": "Bagmati Province",
        "province_np": "बाग्मती प्रदेश",
        
      },
      "district": {
        "id": 29,
        "did": 307,
        
        "district_en": "Bhaktapur",
        "district_np": "भक्तपुर"
      }
    },
    {
      "id": 340,
      "lgid": 30801,
      
      "lgname_en": "Mahalaxmi Municipality",
      "lgname_np": "महालक्ष्मी नगरपालिका",
      "province": {
        "id": 3,
        "province_en": "Bagmati Province",
        "province_np": "बाग्मती प्रदेश",
        
      },
      "district": {
        "id": 30,
        "did": 308,
        
        "district_en": "Lalitpur",
        "district_np": "ललितपुर"
      }
    },
    {
      "id": 341,
      "lgid": 30802,
      
      "lgname_en": "Lalitpur Metro",
      "lgname_np": "ललितपुर महानगरपालिका",
      "province": {
        "id": 3,
        "province_en": "Bagmati Province",
        "province_np": "बाग्मती प्रदेश",
        
      },
      "district": {
        "id": 30,
        "did": 308,
        
        "district_en": "Lalitpur",
        "district_np": "ललितपुर"
      }
    },
    {
      "id": 342,
      "lgid": 30803,
      
      "lgname_en": "Godawari Municipality",
      "lgname_np": "गोदावरी नगरपालिका",
      "province": {
        "id": 3,
        "province_en": "Bagmati Province",
        "province_np": "बाग्मती प्रदेश",
        
      },
      "district": {
        "id": 30,
        "did": 308,
        
        "district_en": "Lalitpur",
        "district_np": "ललितपुर"
      }
    },
    {
      "id": 343,
      "lgid": 30804,
      
      "lgname_en": "Konjyosom Rural Mun",
      "lgname_np": "कोन्ज्योसोम गाउँपालिका",
      "province": {
        "id": 3,
        "province_en": "Bagmati Province",
        "province_np": "बाग्मती प्रदेश",
        
      },
      "district": {
        "id": 30,
        "did": 308,
        
        "district_en": "Lalitpur",
        "district_np": "ललितपुर"
      }
    },
    {
      "id": 344,
      "lgid": 30805,
      
      "lgname_en": "Mahankal Rural Mun",
      "lgname_np": "महाङ्काल गाउँपालिका",
      "province": {
        "id": 3,
        "province_en": "Bagmati Province",
        "province_np": "बाग्मती प्रदेश",
        
      },
      "district": {
        "id": 30,
        "did": 308,
        
        "district_en": "Lalitpur",
        "district_np": "ललितपुर"
      }
    },
    {
      "id": 345,
      "lgid": 30806,
      
      "lgname_en": "Bagmati Rural Mun",
      "lgname_np": "बागमती गाउँपालिका",
      "province": {
        "id": 3,
        "province_en": "Bagmati Province",
        "province_np": "बाग्मती प्रदेश",
        
      },
      "district": {
        "id": 30,
        "did": 308,
        
        "district_en": "Lalitpur",
        "district_np": "ललितपुर"
      }
    },
    {
      "id": 346,
      "lgid": 30901,
      
      "lgname_en": "Chaurideurali Rural Mun",
      "lgname_np": "चौंरीदेउराली गाउँपालिका ",
      "province": {
        "id": 3,
        "province_en": "Bagmati Province",
        "province_np": "बाग्मती प्रदेश",
        
      },
      "district": {
        "id": 31,
        "did": 309,
        
        "district_en": "Kavre",
        "district_np": "काभ्रेपलान्चोक"
      }
    },
    {
      "id": 347,
      "lgid": 30902,
      
      "lgname_en": "Bhumlu Rural Mun",
      "lgname_np": "भुम्लु गाउँपालिका",
      "province": {
        "id": 3,
        "province_en": "Bagmati Province",
        "province_np": "बाग्मती प्रदेश",
        
      },
      "district": {
        "id": 31,
        "did": 309,
        
        "district_en": "Kavre",
        "district_np": "काभ्रेपलान्चोक"
      }
    },
    {
      "id": 348,
      "lgid": 30903,
      
      "lgname_en": "Mandandeupur Municipality",
      "lgname_np": "मण्डनदेउपुर नगरपालिका",
      "province": {
        "id": 3,
        "province_en": "Bagmati Province",
        "province_np": "बाग्मती प्रदेश",
        
      },
      "district": {
        "id": 31,
        "did": 309,
        
        "district_en": "Kavre",
        "district_np": "काभ्रेपलान्चोक"
      }
    },
    {
      "id": 349,
      "lgid": 30904,
      
      "lgname_en": "Banepa Municipality",
      "lgname_np": "बनेपा नगरपालिका",
      "province": {
        "id": 3,
        "province_en": "Bagmati Province",
        "province_np": "बाग्मती प्रदेश",
        
      },
      "district": {
        "id": 31,
        "did": 309,
        
        "district_en": "Kavre",
        "district_np": "काभ्रेपलान्चोक"
      }
    },
    {
      "id": 350,
      "lgid": 30905,
      
      "lgname_en": "Dhulikhel Municipality",
      "lgname_np": "धुलिखेल नगरपालिका",
      "province": {
        "id": 3,
        "province_en": "Bagmati Province",
        "province_np": "बाग्मती प्रदेश",
        
      },
      "district": {
        "id": 31,
        "did": 309,
        
        "district_en": "Kavre",
        "district_np": "काभ्रेपलान्चोक"
      }
    },
    {
      "id": 351,
      "lgid": 30906,
      
      "lgname_en": "Panchkhal Municipality",
      "lgname_np": "पाँचखाल नगरपालिका",
      "province": {
        "id": 3,
        "province_en": "Bagmati Province",
        "province_np": "बाग्मती प्रदेश",
        
      },
      "district": {
        "id": 31,
        "did": 309,
        
        "district_en": "Kavre",
        "district_np": "काभ्रेपलान्चोक"
      }
    },
    {
      "id": 352,
      "lgid": 30907,
      
      "lgname_en": "Temal Rural Mun",
      "lgname_np": "तेमाल गाउँपालिका",
      "province": {
        "id": 3,
        "province_en": "Bagmati Province",
        "province_np": "बाग्मती प्रदेश",
        
      },
      "district": {
        "id": 31,
        "did": 309,
        
        "district_en": "Kavre",
        "district_np": "काभ्रेपलान्चोक"
      }
    },
    {
      "id": 353,
      "lgid": 30908,
      
      "lgname_en": "Namobuddha Municipality",
      "lgname_np": "नमोबुद्ध नगरपालिका",
      "province": {
        "id": 3,
        "province_en": "Bagmati Province",
        "province_np": "बाग्मती प्रदेश",
        
      },
      "district": {
        "id": 31,
        "did": 309,
        
        "district_en": "Kavre",
        "district_np": "काभ्रेपलान्चोक"
      }
    },
    {
      "id": 354,
      "lgid": 30909,
      
      "lgname_en": "Panauti Municipality",
      "lgname_np": "पनौती नगरपालिका",
      "province": {
        "id": 3,
        "province_en": "Bagmati Province",
        "province_np": "बाग्मती प्रदेश",
        
      },
      "district": {
        "id": 31,
        "did": 309,
        
        "district_en": "Kavre",
        "district_np": "काभ्रेपलान्चोक"
      }
    },
    {
      "id": 355,
      "lgid": 30910,
      
      "lgname_en": "Bethanchowk Rural Mun",
      "lgname_np": "बेथानचोक गाउँपालिका",
      "province": {
        "id": 3,
        "province_en": "Bagmati Province",
        "province_np": "बाग्मती प्रदेश",
        
      },
      "district": {
        "id": 31,
        "did": 309,
        
        "district_en": "Kavre",
        "district_np": "काभ्रेपलान्चोक"
      }
    },
    {
      "id": 356,
      "lgid": 30911,
      
      "lgname_en": "Roshi Rural Mun",
      "lgname_np": "रोशी गाउँपालिका",
      "province": {
        "id": 3,
        "province_en": "Bagmati Province",
        "province_np": "बाग्मती प्रदेश",
        
      },
      "district": {
        "id": 31,
        "did": 309,
        
        "district_en": "Kavre",
        "district_np": "काभ्रेपलान्चोक"
      }
    },
    {
      "id": 357,
      "lgid": 30912,
      
      "lgname_en": "Mahabharat Rural Mun",
      "lgname_np": "महाभारत गाँउपालिका",
      "province": {
        "id": 3,
        "province_en": "Bagmati Province",
        "province_np": "बाग्मती प्रदेश",
        
      },
      "district": {
        "id": 31,
        "did": 309,
        
        "district_en": "Kavre",
        "district_np": "काभ्रेपलान्चोक"
      }
    },
    {
      "id": 358,
      "lgid": 30913,
      
      "lgname_en": "Khanikhola Rural Mun",
      "lgname_np": "खानीखोला गाउँपालिका",
      "province": {
        "id": 3,
        "province_en": "Bagmati Province",
        "province_np": "बाग्मती प्रदेश",
        
      },
      "district": {
        "id": 31,
        "did": 309,
        
        "district_en": "Kavre",
        "district_np": "काभ्रेपलान्चोक"
      }
    },
    {
      "id": 359,
      "lgid": 31001,
      
      "lgname_en": "Umakunda Rural Mun",
      "lgname_np": "उमाकुण्ड गाउँपालिका",
      "province": {
        "id": 3,
        "province_en": "Bagmati Province",
        "province_np": "बाग्मती प्रदेश",
        
      },
      "district": {
        "id": 32,
        "did": 310,
        
        "district_en": "Ramechhap",
        "district_np": "रामेछाप"
      }
    },
    {
      "id": 360,
      "lgid": 31002,
      
      "lgname_en": "Gokulganga Rural Mun",
      "lgname_np": "गोकुलगङ्गा गाउँपालिका",
      "province": {
        "id": 3,
        "province_en": "Bagmati Province",
        "province_np": "बाग्मती प्रदेश",
        
      },
      "district": {
        "id": 32,
        "did": 310,
        
        "district_en": "Ramechhap",
        "district_np": "रामेछाप"
      }
    },
    {
      "id": 361,
      "lgid": 31003,
      
      "lgname_en": "Likhu Tamakoshi Rural Mun",
      "lgname_np": "लिखु तामाकोशी गाउँपालिका",
      "province": {
        "id": 3,
        "province_en": "Bagmati Province",
        "province_np": "बाग्मती प्रदेश",
        
      },
      "district": {
        "id": 32,
        "did": 310,
        
        "district_en": "Ramechhap",
        "district_np": "रामेछाप"
      }
    },
    {
      "id": 362,
      "lgid": 31004,
      
      "lgname_en": "Ramechhap Municipality",
      "lgname_np": "रामेछाप नगरपालिका",
      "province": {
        "id": 3,
        "province_en": "Bagmati Province",
        "province_np": "बाग्मती प्रदेश",
        
      },
      "district": {
        "id": 32,
        "did": 310,
        
        "district_en": "Ramechhap",
        "district_np": "रामेछाप"
      }
    },
    {
      "id": 363,
      "lgid": 31005,
      
      "lgname_en": "Manthali Municipality",
      "lgname_np": "मन्थली नगरपालिका",
      "province": {
        "id": 3,
        "province_en": "Bagmati Province",
        "province_np": "बाग्मती प्रदेश",
        
      },
      "district": {
        "id": 32,
        "did": 310,
        
        "district_en": "Ramechhap",
        "district_np": "रामेछाप"
      }
    },
    {
      "id": 364,
      "lgid": 31006,
      
      "lgname_en": "Khandadevi Rural Mun",
      "lgname_np": "खाँडादेवी गाउँपालिका",
      "province": {
        "id": 3,
        "province_en": "Bagmati Province",
        "province_np": "बाग्मती प्रदेश",
        
      },
      "district": {
        "id": 32,
        "did": 310,
        
        "district_en": "Ramechhap",
        "district_np": "रामेछाप"
      }
    },
    {
      "id": 365,
      "lgid": 31007,
      
      "lgname_en": "Doramba Rural Mun",
      "lgname_np": "दोरम्बा शैंलुङ गाउँपालिका",
      "province": {
        "id": 3,
        "province_en": "Bagmati Province",
        "province_np": "बाग्मती प्रदेश",
        
      },
      "district": {
        "id": 32,
        "did": 310,
        
        "district_en": "Ramechhap",
        "district_np": "रामेछाप"
      }
    },
    {
      "id": 366,
      "lgid": 31008,
      
      "lgname_en": "Sunapati Rural Mun",
      "lgname_np": "सुनापती गाउँपालिका",
      "province": {
        "id": 3,
        "province_en": "Bagmati Province",
        "province_np": "बाग्मती प्रदेश",
        
      },
      "district": {
        "id": 32,
        "did": 310,
        
        "district_en": "Ramechhap",
        "district_np": "रामेछाप"
      }
    },
    {
      "id": 367,
      "lgid": 31101,
      
      "lgname_en": "Dudhauli Municipality",
      "lgname_np": "दुधौली नगरपालिका",
      "province": {
        "id": 3,
        "province_en": "Bagmati Province",
        "province_np": "बाग्मती प्रदेश",
        
      },
      "district": {
        "id": 33,
        "did": 311,
        
        "district_en": "Sindhuli",
        "district_np": "सिन्धुली"
      }
    },
    {
      "id": 368,
      "lgid": 31102,
      
      "lgname_en": "Phikkal Rural Mun",
      "lgname_np": "फिक्कल गाउँपालिका",
      "province": {
        "id": 3,
        "province_en": "Bagmati Province",
        "province_np": "बाग्मती प्रदेश",
        
      },
      "district": {
        "id": 33,
        "did": 311,
        
        "district_en": "Sindhuli",
        "district_np": "सिन्धुली"
      }
    },
    {
      "id": 369,
      "lgid": 31103,
      
      "lgname_en": "Tinpatan Rural Mun",
      "lgname_np": "तीनपाटन गाउँपालिका",
      "province": {
        "id": 3,
        "province_en": "Bagmati Province",
        "province_np": "बाग्मती प्रदेश",
        
      },
      "district": {
        "id": 33,
        "did": 311,
        
        "district_en": "Sindhuli",
        "district_np": "सिन्धुली"
      }
    },
    {
      "id": 370,
      "lgid": 31104,
      
      "lgname_en": "Golanjor Rural Mun",
      "lgname_np": "गोलन्जर गाउँपालिका",
      "province": {
        "id": 3,
        "province_en": "Bagmati Province",
        "province_np": "बाग्मती प्रदेश",
        
      },
      "district": {
        "id": 33,
        "did": 311,
        
        "district_en": "Sindhuli",
        "district_np": "सिन्धुली"
      }
    },
    {
      "id": 371,
      "lgid": 31105,
      
      "lgname_en": "Kamalamai Municipality",
      "lgname_np": "कमलामाई नगरपालिका",
      "province": {
        "id": 3,
        "province_en": "Bagmati Province",
        "province_np": "बाग्मती प्रदेश",
        
      },
      "district": {
        "id": 33,
        "did": 311,
        
        "district_en": "Sindhuli",
        "district_np": "सिन्धुली"
      }
    },
    {
      "id": 372,
      "lgid": 31106,
      
      "lgname_en": "Sunkoshi Rural Mun",
      "lgname_np": "सुनकोशी गाउँपालिका",
      "province": {
        "id": 3,
        "province_en": "Bagmati Province",
        "province_np": "बाग्मती प्रदेश",
        
      },
      "district": {
        "id": 33,
        "did": 311,
        
        "district_en": "Sindhuli",
        "district_np": "सिन्धुली"
      }
    },
    {
      "id": 373,
      "lgid": 31107,
      
      "lgname_en": "Ghyanglekh Rural Mun",
      "lgname_np": "घ्याङलेख गाउँपालिका",
      "province": {
        "id": 3,
        "province_en": "Bagmati Province",
        "province_np": "बाग्मती प्रदेश",
        
      },
      "district": {
        "id": 33,
        "did": 311,
        
        "district_en": "Sindhuli",
        "district_np": "सिन्धुली"
      }
    },
    {
      "id": 374,
      "lgid": 31108,
      
      "lgname_en": "Marin Rural Mun",
      "lgname_np": "मरिण गाउँपालिका",
      "province": {
        "id": 3,
        "province_en": "Bagmati Province",
        "province_np": "बाग्मती प्रदेश",
        
      },
      "district": {
        "id": 33,
        "did": 311,
        
        "district_en": "Sindhuli",
        "district_np": "सिन्धुली"
      }
    },
    {
      "id": 375,
      "lgid": 31109,
      
      "lgname_en": "Hariharpurgadhi Rural Mun",
      "lgname_np": "हरिहरपुरगढी गाउँपालिका",
      "province": {
        "id": 3,
        "province_en": "Bagmati Province",
        "province_np": "बाग्मती प्रदेश",
        
      },
      "district": {
        "id": 33,
        "did": 311,
        
        "district_en": "Sindhuli",
        "district_np": "सिन्धुली"
      }
    },
    {
      "id": 376,
      "lgid": 31201,
      
      "lgname_en": "Indrasarowar Rural Mun",
      "lgname_np": "इन्द्रसरोबर गाउँपालिका",
      "province": {
        "id": 3,
        "province_en": "Bagmati Province",
        "province_np": "बाग्मती प्रदेश",
        
      },
      "district": {
        "id": 34,
        "did": 312,
        
        "district_en": "Makwanpur",
        "district_np": "मकवानपुर"
      }
    },
    {
      "id": 377,
      "lgid": 31202,
      
      "lgname_en": "Thaha Municipality",
      "lgname_np": "थाहा नगरपालिका",
      "province": {
        "id": 3,
        "province_en": "Bagmati Province",
        "province_np": "बाग्मती प्रदेश",
        
      },
      "district": {
        "id": 34,
        "did": 312,
        
        "district_en": "Makwanpur",
        "district_np": "मकवानपुर"
      }
    },
    {
      "id": 378,
      "lgid": 31203,
      
      "lgname_en": "Kailash Rural Mun",
      "lgname_np": "कैलाश गाउँपालिका",
      "province": {
        "id": 3,
        "province_en": "Bagmati Province",
        "province_np": "बाग्मती प्रदेश",
        
      },
      "district": {
        "id": 34,
        "did": 312,
        
        "district_en": "Makwanpur",
        "district_np": "मकवानपुर"
      }
    },
    {
      "id": 379,
      "lgid": 31204,
      
      "lgname_en": "Raksirang Rural Mun",
      "lgname_np": "राक्सिराङ्ग गाउँपालिका",
      "province": {
        "id": 3,
        "province_en": "Bagmati Province",
        "province_np": "बाग्मती प्रदेश",
        
      },
      "district": {
        "id": 34,
        "did": 312,
        
        "district_en": "Makwanpur",
        "district_np": "मकवानपुर"
      }
    },
    {
      "id": 380,
      "lgid": 31205,
      
      "lgname_en": "Manahari Rural Mun",
      "lgname_np": "मनहरी गाउँपालिका",
      "province": {
        "id": 3,
        "province_en": "Bagmati Province",
        "province_np": "बाग्मती प्रदेश",
        
      },
      "district": {
        "id": 34,
        "did": 312,
        
        "district_en": "Makwanpur",
        "district_np": "मकवानपुर"
      }
    },
    {
      "id": 381,
      "lgid": 31206,
      
      "lgname_en": "Hetauda Sub-Metro",
      "lgname_np": "हेटौडा उपमहानगरपालिका",
      "province": {
        "id": 3,
        "province_en": "Bagmati Province",
        "province_np": "बाग्मती प्रदेश",
        
      },
      "district": {
        "id": 34,
        "did": 312,
        
        "district_en": "Makwanpur",
        "district_np": "मकवानपुर"
      }
    },
    {
      "id": 382,
      "lgid": 31207,
      
      "lgname_en": "Bhimphedi Rural Mun",
      "lgname_np": "भिमफेदी गाउँपालिका",
      "province": {
        "id": 3,
        "province_en": "Bagmati Province",
        "province_np": "बाग्मती प्रदेश",
        
      },
      "district": {
        "id": 34,
        "did": 312,
        
        "district_en": "Makwanpur",
        "district_np": "मकवानपुर"
      }
    },
    {
      "id": 383,
      "lgid": 31208,
      
      "lgname_en": "Makawanpurgadhi Rural Mun",
      "lgname_np": "मकवानपुरगढी गाउँपालिका",
      "province": {
        "id": 3,
        "province_en": "Bagmati Province",
        "province_np": "बाग्मती प्रदेश",
        
      },
      "district": {
        "id": 34,
        "did": 312,
        
        "district_en": "Makwanpur",
        "district_np": "मकवानपुर"
      }
    },
    {
      "id": 384,
      "lgid": 31209,
      
      "lgname_en": "Bakaiya Rural Mun",
      "lgname_np": "बकैया गाउँपालिका",
      "province": {
        "id": 3,
        "province_en": "Bagmati Province",
        "province_np": "बाग्मती प्रदेश",
        
      },
      "district": {
        "id": 34,
        "did": 312,
        
        "district_en": "Makwanpur",
        "district_np": "मकवानपुर"
      }
    },
    {
      "id": 385,
      "lgid": 31210,
      
      "lgname_en": "Bagmati Rural Mun",
      "lgname_np": "बाग्मति गाउँपालिका",
      "province": {
        "id": 3,
        "province_en": "Bagmati Province",
        "province_np": "बाग्मती प्रदेश",
        
      },
      "district": {
        "id": 34,
        "did": 312,
        
        "district_en": "Makwanpur",
        "district_np": "मकवानपुर"
      }
    },
    {
      "id": 386,
      "lgid": 31301,
      
      "lgname_en": "Rapti Municipality",
      "lgname_np": "राप्ती नगरपालिका",
      "province": {
        "id": 3,
        "province_en": "Bagmati Province",
        "province_np": "बाग्मती प्रदेश",
        
      },
      "district": {
        "id": 35,
        "did": 313,
        
        "district_en": "Chitwan",
        "district_np": "चितवन"
      }
    },
    {
      "id": 387,
      "lgid": 31302,
      
      "lgname_en": "Kalika Municipality",
      "lgname_np": "कालिका नगरपालिका",
      "province": {
        "id": 3,
        "province_en": "Bagmati Province",
        "province_np": "बाग्मती प्रदेश",
        
      },
      "district": {
        "id": 35,
        "did": 313,
        
        "district_en": "Chitwan",
        "district_np": "चितवन"
      }
    },
    {
      "id": 388,
      "lgid": 31303,
      
      "lgname_en": "Ichchhakamana Rural Mun",
      "lgname_np": "इच्छाकामना गाउँपालिका",
      "province": {
        "id": 3,
        "province_en": "Bagmati Province",
        "province_np": "बाग्मती प्रदेश",
        
      },
      "district": {
        "id": 35,
        "did": 313,
        
        "district_en": "Chitwan",
        "district_np": "चितवन"
      }
    },
    {
      "id": 389,
      "lgid": 31304,
      
      "lgname_en": "Bharatpur Metro",
      "lgname_np": "भरतपुर महानगरपालिका",
      "province": {
        "id": 3,
        "province_en": "Bagmati Province",
        "province_np": "बाग्मती प्रदेश",
        
      },
      "district": {
        "id": 35,
        "did": 313,
        
        "district_en": "Chitwan",
        "district_np": "चितवन"
      }
    },
    {
      "id": 390,
      "lgid": 31305,
      
      "lgname_en": "Ratnanagar Municipality",
      "lgname_np": "रत्ननगर नगरपालिका",
      "province": {
        "id": 3,
        "province_en": "Bagmati Province",
        "province_np": "बाग्मती प्रदेश",
        
      },
      "district": {
        "id": 35,
        "did": 313,
        
        "district_en": "Chitwan",
        "district_np": "चितवन"
      }
    },
    {
      "id": 391,
      "lgid": 31306,
      
      "lgname_en": "Khairhani Municipality",
      "lgname_np": "खैरहनी नगरपालिका",
      "province": {
        "id": 3,
        "province_en": "Bagmati Province",
        "province_np": "बाग्मती प्रदेश",
        
      },
      "district": {
        "id": 35,
        "did": 313,
        
        "district_en": "Chitwan",
        "district_np": "चितवन"
      }
    },
    {
      "id": 392,
      "lgid": 31307,
      
      "lgname_en": "Madi Municipality",
      "lgname_np": "माडी नगरपालिका",
      "province": {
        "id": 3,
        "province_en": "Bagmati Province",
        "province_np": "बाग्मती प्रदेश",
        
      },
      "district": {
        "id": 35,
        "did": 313,
        
        "district_en": "Chitwan",
        "district_np": "चितवन"
      }
    },
    {
      "id": 393,
      "lgid": 40101,
      
      "lgname_en": "Chumanuwri Rural Mun",
      "lgname_np": "चुमनुव्री गाउँपालिका",
      "province": {
        "id": 4,
        "province_en": "Gandaki Province",
        "province_np": "गण्डकी प्रदेश",
        
      },
      "district": {
        "id": 36,
        "did": 401,
        
        "district_en": "Gorkha",
        "district_np": "गोरखा"
      }
    },
    {
      "id": 394,
      "lgid": 40102,
      
      "lgname_en": "Ajirkot Rural Mun",
      "lgname_np": "अजिरकोट गाउँपालिका",
      "province": {
        "id": 4,
        "province_en": "Gandaki Province",
        "province_np": "गण्डकी प्रदेश",
        
      },
      "district": {
        "id": 36,
        "did": 401,
        
        "district_en": "Gorkha",
        "district_np": "गोरखा"
      }
    },
    {
      "id": 395,
      "lgid": 40103,
      
      "lgname_en": "Barpak Sulikot Rural Mun",
      "lgname_np": "बारपाक सुलिकोट गाउँपालिका",
      "province": {
        "id": 4,
        "province_en": "Gandaki Province",
        "province_np": "गण्डकी प्रदेश",
        
      },
      "district": {
        "id": 36,
        "did": 401,
        
        "district_en": "Gorkha",
        "district_np": "गोरखा"
      }
    },
    {
      "id": 396,
      "lgid": 40104,
      
      "lgname_en": "Dharche Rural Mun",
      "lgname_np": "धार्चे गाउँपालिका",
      "province": {
        "id": 4,
        "province_en": "Gandaki Province",
        "province_np": "गण्डकी प्रदेश",
        
      },
      "district": {
        "id": 36,
        "did": 401,
        
        "district_en": "Gorkha",
        "district_np": "गोरखा"
      }
    },
    {
      "id": 397,
      "lgid": 40105,
      
      "lgname_en": "Aarughat Rural Mun",
      "lgname_np": "आरूघाट गाउँपालिका",
      "province": {
        "id": 4,
        "province_en": "Gandaki Province",
        "province_np": "गण्डकी प्रदेश",
        
      },
      "district": {
        "id": 36,
        "did": 401,
        
        "district_en": "Gorkha",
        "district_np": "गोरखा"
      }
    },
    {
      "id": 398,
      "lgid": 40106,
      
      "lgname_en": "Bhimsenthapa Rural Mun",
      "lgname_np": "भिमसेनथापा गाउँपालिका",
      "province": {
        "id": 4,
        "province_en": "Gandaki Province",
        "province_np": "गण्डकी प्रदेश",
        
      },
      "district": {
        "id": 36,
        "did": 401,
        
        "district_en": "Gorkha",
        "district_np": "गोरखा"
      }
    },
    {
      "id": 399,
      "lgid": 40107,
      
      "lgname_en": "Siranchowk Rural Mun",
      "lgname_np": "सिरानचोक गाउँपालिका",
      "province": {
        "id": 4,
        "province_en": "Gandaki Province",
        "province_np": "गण्डकी प्रदेश",
        
      },
      "district": {
        "id": 36,
        "did": 401,
        
        "district_en": "Gorkha",
        "district_np": "गोरखा"
      }
    },
    {
      "id": 400,
      "lgid": 40108,
      
      "lgname_en": "Palungtar Municipality",
      "lgname_np": "पालुङटार नगरपालिका",
      "province": {
        "id": 4,
        "province_en": "Gandaki Province",
        "province_np": "गण्डकी प्रदेश",
        
      },
      "district": {
        "id": 36,
        "did": 401,
        
        "district_en": "Gorkha",
        "district_np": "गोरखा"
      }
    },
    {
      "id": 401,
      "lgid": 40109,
      
      "lgname_en": "Gorkha Municipality",
      "lgname_np": "गोरखा नगरपालिका",
      "province": {
        "id": 4,
        "province_en": "Gandaki Province",
        "province_np": "गण्डकी प्रदेश",
        
      },
      "district": {
        "id": 36,
        "did": 401,
        
        "district_en": "Gorkha",
        "district_np": "गोरखा"
      }
    },
    {
      "id": 402,
      "lgid": 40110,
      
      "lgname_en": "Shahidlakhan Rural Mun",
      "lgname_np": "शहिद लखन गाउँपालिका",
      "province": {
        "id": 4,
        "province_en": "Gandaki Province",
        "province_np": "गण्डकी प्रदेश",
        
      },
      "district": {
        "id": 36,
        "did": 401,
        
        "district_en": "Gorkha",
        "district_np": "गोरखा"
      }
    },
    {
      "id": 403,
      "lgid": 40111,
      
      "lgname_en": "Gandaki Rural Mun",
      "lgname_np": "गण्डकी गाउँपालिका",
      "province": {
        "id": 4,
        "province_en": "Gandaki Province",
        "province_np": "गण्डकी प्रदेश",
        
      },
      "district": {
        "id": 36,
        "did": 401,
        
        "district_en": "Gorkha",
        "district_np": "गोरखा"
      }
    },
    {
      "id": 404,
      "lgid": 40201,
      
      "lgname_en": "Narpa Bhumi Rural Mun",
      "lgname_np": "नार्पा भूमि गाउँपालिका",
      "province": {
        "id": 4,
        "province_en": "Gandaki Province",
        "province_np": "गण्डकी प्रदेश",
        
      },
      "district": {
        "id": 37,
        "did": 402,
        
        "district_en": "Manang",
        "district_np": "मनाङ"
      }
    },
    {
      "id": 405,
      "lgid": 40202,
      
      "lgname_en": "Manang Ngisyang Rural Mun",
      "lgname_np": "मनाङ ङिस्याङ गाउँपालिका",
      "province": {
        "id": 4,
        "province_en": "Gandaki Province",
        "province_np": "गण्डकी प्रदेश",
        
      },
      "district": {
        "id": 37,
        "did": 402,
        
        "district_en": "Manang",
        "district_np": "मनाङ"
      }
    },
    {
      "id": 406,
      "lgid": 40203,
      
      "lgname_en": "Chame Rural Mun",
      "lgname_np": "चामे गाउँपालिका ",
      "province": {
        "id": 4,
        "province_en": "Gandaki Province",
        "province_np": "गण्डकी प्रदेश",
        
      },
      "district": {
        "id": 37,
        "did": 402,
        
        "district_en": "Manang",
        "district_np": "मनाङ"
      }
    },
    {
      "id": 407,
      "lgid": 40204,
      
      "lgname_en": "Nason Rural Mun",
      "lgname_np": "नासोँ गाउँपालिका",
      "province": {
        "id": 4,
        "province_en": "Gandaki Province",
        "province_np": "गण्डकी प्रदेश",
        
      },
      "district": {
        "id": 37,
        "did": 402,
        
        "district_en": "Manang",
        "district_np": "मनाङ"
      }
    },
    {
      "id": 408,
      "lgid": 40301,
      
      "lgname_en": "Lo Ghekar Damodarkunda Rural Mun",
      "lgname_np": "लो-घेकर दामोदरकुण्ड गाउँपालिका",
      "province": {
        "id": 4,
        "province_en": "Gandaki Province",
        "province_np": "गण्डकी प्रदेश",
        
      },
      "district": {
        "id": 38,
        "did": 403,
        
        "district_en": "Mustang",
        "district_np": "मुस्ताङ"
      }
    },
    {
      "id": 409,
      "lgid": 40302,
      
      "lgname_en": "Gharpajhong Rural Mun",
      "lgname_np": "घरपझोङ गाउँपालिका",
      "province": {
        "id": 4,
        "province_en": "Gandaki Province",
        "province_np": "गण्डकी प्रदेश",
        
      },
      "district": {
        "id": 38,
        "did": 403,
        
        "district_en": "Mustang",
        "district_np": "मुस्ताङ"
      }
    },
    {
      "id": 410,
      "lgid": 40303,
      
      "lgname_en": "Varagung Muktichhetra Rural Mun",
      "lgname_np": "वारागुङ मुक्तिक्षेत्र गाउँपालिका",
      "province": {
        "id": 4,
        "province_en": "Gandaki Province",
        "province_np": "गण्डकी प्रदेश",
        
      },
      "district": {
        "id": 38,
        "did": 403,
        
        "district_en": "Mustang",
        "district_np": "मुस्ताङ"
      }
    },
    {
      "id": 411,
      "lgid": 40304,
      
      "lgname_en": "Lomanthang Rural Mun",
      "lgname_np": "लोमन्थाङ गाउँपालिका",
      "province": {
        "id": 4,
        "province_en": "Gandaki Province",
        "province_np": "गण्डकी प्रदेश",
        
      },
      "district": {
        "id": 38,
        "did": 403,
        
        "district_en": "Mustang",
        "district_np": "मुस्ताङ"
      }
    },
    {
      "id": 412,
      "lgid": 40305,
      
      "lgname_en": "Thasang Rural Mun",
      "lgname_np": "थासाङ गाउँपालिका",
      "province": {
        "id": 4,
        "province_en": "Gandaki Province",
        "province_np": "गण्डकी प्रदेश",
        
      },
      "district": {
        "id": 38,
        "did": 403,
        
        "district_en": "Mustang",
        "district_np": "मुस्ताङ"
      }
    },
    {
      "id": 413,
      "lgid": 40401,
      
      "lgname_en": "Annapurna Rural Mun",
      "lgname_np": "अन्नपुर्ण गाउँपालिका",
      "province": {
        "id": 4,
        "province_en": "Gandaki Province",
        "province_np": "गण्डकी प्रदेश",
        
      },
      "district": {
        "id": 39,
        "did": 404,
        
        "district_en": "Myagdi",
        "district_np": "म्याग्दी"
      }
    },
    {
      "id": 414,
      "lgid": 40402,
      
      "lgname_en": "Raghuganga Rural Mun",
      "lgname_np": "रघुगंगा गाउँपालिका",
      "province": {
        "id": 4,
        "province_en": "Gandaki Province",
        "province_np": "गण्डकी प्रदेश",
        
      },
      "district": {
        "id": 39,
        "did": 404,
        
        "district_en": "Myagdi",
        "district_np": "म्याग्दी"
      }
    },
    {
      "id": 415,
      "lgid": 40403,
      
      "lgname_en": "Dhawalagiri Rural Mun",
      "lgname_np": "धवलागिरी गाउँपालिका",
      "province": {
        "id": 4,
        "province_en": "Gandaki Province",
        "province_np": "गण्डकी प्रदेश",
        
      },
      "district": {
        "id": 39,
        "did": 404,
        
        "district_en": "Myagdi",
        "district_np": "म्याग्दी"
      }
    },
    {
      "id": 416,
      "lgid": 40404,
      
      "lgname_en": "Malika Rural Mun",
      "lgname_np": "मालिका गाउँपालिका",
      "province": {
        "id": 4,
        "province_en": "Gandaki Province",
        "province_np": "गण्डकी प्रदेश",
        
      },
      "district": {
        "id": 39,
        "did": 404,
        
        "district_en": "Myagdi",
        "district_np": "म्याग्दी"
      }
    },
    {
      "id": 417,
      "lgid": 40405,
      
      "lgname_en": "Mangala Rural Mun",
      "lgname_np": "मंगला गाउँपालिका",
      "province": {
        "id": 4,
        "province_en": "Gandaki Province",
        "province_np": "गण्डकी प्रदेश",
        
      },
      "district": {
        "id": 39,
        "did": 404,
        
        "district_en": "Myagdi",
        "district_np": "म्याग्दी"
      }
    },
    {
      "id": 418,
      "lgid": 40406,
      
      "lgname_en": "Beni Municipality",
      "lgname_np": "बेनी नगरपालिका",
      "province": {
        "id": 4,
        "province_en": "Gandaki Province",
        "province_np": "गण्डकी प्रदेश",
        
      },
      "district": {
        "id": 39,
        "did": 404,
        
        "district_en": "Myagdi",
        "district_np": "म्याग्दी"
      }
    },
    {
      "id": 419,
      "lgid": 40501,
      
      "lgname_en": "Madi Rural Mun",
      "lgname_np": "मादी गाउँपालिका",
      "province": {
        "id": 4,
        "province_en": "Gandaki Province",
        "province_np": "गण्डकी प्रदेश",
        
      },
      "district": {
        "id": 40,
        "did": 405,
        
        "district_en": "Kaski",
        "district_np": "कास्की"
      }
    },
    {
      "id": 420,
      "lgid": 40502,
      
      "lgname_en": "Machhapuchhre Rural Mun",
      "lgname_np": "माछापुच्छ्रे गाउँपालिका",
      "province": {
        "id": 4,
        "province_en": "Gandaki Province",
        "province_np": "गण्डकी प्रदेश",
        
      },
      "district": {
        "id": 40,
        "did": 405,
        
        "district_en": "Kaski",
        "district_np": "कास्की"
      }
    },
    {
      "id": 421,
      "lgid": 40503,
      
      "lgname_en": "Annapurna Rural Mun",
      "lgname_np": "अन्नपूर्ण गाउँपालिका",
      "province": {
        "id": 4,
        "province_en": "Gandaki Province",
        "province_np": "गण्डकी प्रदेश",
        
      },
      "district": {
        "id": 40,
        "did": 405,
        
        "district_en": "Kaski",
        "district_np": "कास्की"
      }
    },
    {
      "id": 422,
      "lgid": 40504,
      
      "lgname_en": "Pokhara Metro",
      "lgname_np": "पोखरा महानगरपालिका",
      "province": {
        "id": 4,
        "province_en": "Gandaki Province",
        "province_np": "गण्डकी प्रदेश",
        
      },
      "district": {
        "id": 40,
        "did": 405,
        
        "district_en": "Kaski",
        "district_np": "कास्की"
      }
    },
    {
      "id": 423,
      "lgid": 40505,
      
      "lgname_en": "Rupa Rural Mun",
      "lgname_np": "रूपा गाउँपालिका",
      "province": {
        "id": 4,
        "province_en": "Gandaki Province",
        "province_np": "गण्डकी प्रदेश",
        
      },
      "district": {
        "id": 40,
        "did": 405,
        
        "district_en": "Kaski",
        "district_np": "कास्की"
      }
    },
    {
      "id": 424,
      "lgid": 40601,
      
      "lgname_en": "Dordi Rural Mun",
      "lgname_np": "दोर्दी गाउँपालिका",
      "province": {
        "id": 4,
        "province_en": "Gandaki Province",
        "province_np": "गण्डकी प्रदेश",
        
      },
      "district": {
        "id": 41,
        "did": 406,
        
        "district_en": "Lamjung",
        "district_np": "लमजुङ"
      }
    },
    {
      "id": 425,
      "lgid": 40602,
      
      "lgname_en": "Marsyangdi Rural Mun",
      "lgname_np": "मर्स्याङदी गाउँपालिका",
      "province": {
        "id": 4,
        "province_en": "Gandaki Province",
        "province_np": "गण्डकी प्रदेश",
        
      },
      "district": {
        "id": 41,
        "did": 406,
        
        "district_en": "Lamjung",
        "district_np": "लमजुङ"
      }
    },
    {
      "id": 426,
      "lgid": 40603,
      
      "lgname_en": "Kwholasothar Rural Mun",
      "lgname_np": "क्व्होलासोथार गाउँपालिका",
      "province": {
        "id": 4,
        "province_en": "Gandaki Province",
        "province_np": "गण्डकी प्रदेश",
        
      },
      "district": {
        "id": 41,
        "did": 406,
        
        "district_en": "Lamjung",
        "district_np": "लमजुङ"
      }
    },
    {
      "id": 427,
      "lgid": 40604,
      
      "lgname_en": "Madhyanepal Municipality",
      "lgname_np": "मध्यनेपाल नगरपालिका",
      "province": {
        "id": 4,
        "province_en": "Gandaki Province",
        "province_np": "गण्डकी प्रदेश",
        
      },
      "district": {
        "id": 41,
        "did": 406,
        
        "district_en": "Lamjung",
        "district_np": "लमजुङ"
      }
    },
    {
      "id": 428,
      "lgid": 40605,
      
      "lgname_en": "Besishahar Municipality",
      "lgname_np": "बेसीशहर नगरपालिका",
      "province": {
        "id": 4,
        "province_en": "Gandaki Province",
        "province_np": "गण्डकी प्रदेश",
        
      },
      "district": {
        "id": 41,
        "did": 406,
        
        "district_en": "Lamjung",
        "district_np": "लमजुङ"
      }
    },
    {
      "id": 429,
      "lgid": 40606,
      
      "lgname_en": "Sundarbazar Municipality",
      "lgname_np": "सुन्दरबजार नगरपालिका",
      "province": {
        "id": 4,
        "province_en": "Gandaki Province",
        "province_np": "गण्डकी प्रदेश",
        
      },
      "district": {
        "id": 41,
        "did": 406,
        
        "district_en": "Lamjung",
        "district_np": "लमजुङ"
      }
    },
    {
      "id": 430,
      "lgid": 40607,
      
      "lgname_en": "Rainas Municipality",
      "lgname_np": "राईनास नगरपालिका",
      "province": {
        "id": 4,
        "province_en": "Gandaki Province",
        "province_np": "गण्डकी प्रदेश",
        
      },
      "district": {
        "id": 41,
        "did": 406,
        
        "district_en": "Lamjung",
        "district_np": "लमजुङ"
      }
    },
    {
      "id": 431,
      "lgid": 40608,
      
      "lgname_en": "Dudhpokhari Rural Mun",
      "lgname_np": "दूधपोखरी गाउँपालिका",
      "province": {
        "id": 4,
        "province_en": "Gandaki Province",
        "province_np": "गण्डकी प्रदेश",
        
      },
      "district": {
        "id": 41,
        "did": 406,
        
        "district_en": "Lamjung",
        "district_np": "लमजुङ"
      }
    },
    {
      "id": 432,
      "lgid": 40701,
      
      "lgname_en": "Bhanu Municipality",
      "lgname_np": "भानु नगरपालिका",
      "province": {
        "id": 4,
        "province_en": "Gandaki Province",
        "province_np": "गण्डकी प्रदेश",
        
      },
      "district": {
        "id": 42,
        "did": 407,
        
        "district_en": "Tanahun",
        "district_np": "तनहुँ"
      }
    },
    {
      "id": 433,
      "lgid": 40702,
      
      "lgname_en": "Vyas Municipality",
      "lgname_np": "व्यास नगरपालिका",
      "province": {
        "id": 4,
        "province_en": "Gandaki Province",
        "province_np": "गण्डकी प्रदेश",
        
      },
      "district": {
        "id": 42,
        "did": 407,
        
        "district_en": "Tanahun",
        "district_np": "तनहुँ"
      }
    },
    {
      "id": 434,
      "lgid": 40703,
      
      "lgname_en": "Myagde Rural Mun",
      "lgname_np": "म्याग्दे गाउँपालिका",
      "province": {
        "id": 4,
        "province_en": "Gandaki Province",
        "province_np": "गण्डकी प्रदेश",
        
      },
      "district": {
        "id": 42,
        "did": 407,
        
        "district_en": "Tanahun",
        "district_np": "तनहुँ"
      }
    },
    {
      "id": 435,
      "lgid": 40704,
      
      "lgname_en": "Shuklagandaki Municipality",
      "lgname_np": "शुक्लागण्डकी नगरपालिका",
      "province": {
        "id": 4,
        "province_en": "Gandaki Province",
        "province_np": "गण्डकी प्रदेश",
        
      },
      "district": {
        "id": 42,
        "did": 407,
        
        "district_en": "Tanahun",
        "district_np": "तनहुँ"
      }
    },
    {
      "id": 436,
      "lgid": 40705,
      
      "lgname_en": "Bhimad Municipality",
      "lgname_np": "भिमाद नगरपालिका",
      "province": {
        "id": 4,
        "province_en": "Gandaki Province",
        "province_np": "गण्डकी प्रदेश",
        
      },
      "district": {
        "id": 42,
        "did": 407,
        
        "district_en": "Tanahun",
        "district_np": "तनहुँ"
      }
    },
    {
      "id": 437,
      "lgid": 40706,
      
      "lgname_en": "Ghiring Rural Mun",
      "lgname_np": "घिरिङ गाउँपालिका",
      "province": {
        "id": 4,
        "province_en": "Gandaki Province",
        "province_np": "गण्डकी प्रदेश",
        
      },
      "district": {
        "id": 42,
        "did": 407,
        
        "district_en": "Tanahun",
        "district_np": "तनहुँ"
      }
    },
    {
      "id": 438,
      "lgid": 40707,
      
      "lgname_en": "Rishing Rural Mun",
      "lgname_np": "ऋषिङ्ग गाउँपालिका",
      "province": {
        "id": 4,
        "province_en": "Gandaki Province",
        "province_np": "गण्डकी प्रदेश",
        
      },
      "district": {
        "id": 42,
        "did": 407,
        
        "district_en": "Tanahun",
        "district_np": "तनहुँ"
      }
    },
    {
      "id": 439,
      "lgid": 40708,
      
      "lgname_en": "Devghat Rural Mun",
      "lgname_np": "देवघाट गाउँपालिका",
      "province": {
        "id": 4,
        "province_en": "Gandaki Province",
        "province_np": "गण्डकी प्रदेश",
        
      },
      "district": {
        "id": 42,
        "did": 407,
        
        "district_en": "Tanahun",
        "district_np": "तनहुँ"
      }
    },
    {
      "id": 440,
      "lgid": 40709,
      
      "lgname_en": "Bandipur Rural Mun",
      "lgname_np": "वन्दिपुर गाउँपालिका",
      "province": {
        "id": 4,
        "province_en": "Gandaki Province",
        "province_np": "गण्डकी प्रदेश",
        
      },
      "district": {
        "id": 42,
        "did": 407,
        
        "district_en": "Tanahun",
        "district_np": "तनहुँ"
      }
    },
    {
      "id": 441,
      "lgid": 40710,
      
      "lgname_en": "Aanbookhaireni Rural Mun",
      "lgname_np": "आँबुखैरेनी गाउँपालिका",
      "province": {
        "id": 4,
        "province_en": "Gandaki Province",
        "province_np": "गण्डकी प्रदेश",
        
      },
      "district": {
        "id": 42,
        "did": 407,
        
        "district_en": "Tanahun",
        "district_np": "तनहुँ"
      }
    },
    {
      "id": 442,
      "lgid": 40801,
      
      "lgname_en": "Gaidakot Municipality",
      "lgname_np": "गैडाकोट नगरपालिका",
      "province": {
        "id": 4,
        "province_en": "Gandaki Province",
        "province_np": "गण्डकी प्रदेश",
        
      },
      "district": {
        "id": 43,
        "did": 408,
        
        "district_en": "Nawalparasi (East)",
        "district_np": "नवलपरासी (बर्दघाट सुस्ता पूर्व)"
      }
    },
    {
      "id": 443,
      "lgid": 40802,
      
      "lgname_en": "Bulingtar Rural Mun",
      "lgname_np": "बुलिङटार गाउँपालिका",
      "province": {
        "id": 4,
        "province_en": "Gandaki Province",
        "province_np": "गण्डकी प्रदेश",
        
      },
      "district": {
        "id": 43,
        "did": 408,
        
        "district_en": "Nawalparasi (East)",
        "district_np": "नवलपरासी (बर्दघाट सुस्ता पूर्व)"
      }
    },
    {
      "id": 444,
      "lgid": 40803,
      
      "lgname_en": "Baudikali Rural Mun",
      "lgname_np": "बौदीकाली गाउँपालिका",
      "province": {
        "id": 4,
        "province_en": "Gandaki Province",
        "province_np": "गण्डकी प्रदेश",
        
      },
      "district": {
        "id": 43,
        "did": 408,
        
        "district_en": "Nawalparasi (East)",
        "district_np": "नवलपरासी (बर्दघाट सुस्ता पूर्व)"
      }
    },
    {
      "id": 445,
      "lgid": 40804,
      
      "lgname_en": "Hupsekot Rural Mun",
      "lgname_np": "हुप्सेकोट गाउँपालिका",
      "province": {
        "id": 4,
        "province_en": "Gandaki Province",
        "province_np": "गण्डकी प्रदेश",
        
      },
      "district": {
        "id": 43,
        "did": 408,
        
        "district_en": "Nawalparasi (East)",
        "district_np": "नवलपरासी (बर्दघाट सुस्ता पूर्व)"
      }
    },
    {
      "id": 446,
      "lgid": 40805,
      
      "lgname_en": "Devchuli Municipality",
      "lgname_np": "देवचुली नगरपालिका",
      "province": {
        "id": 4,
        "province_en": "Gandaki Province",
        "province_np": "गण्डकी प्रदेश",
        
      },
      "district": {
        "id": 43,
        "did": 408,
        
        "district_en": "Nawalparasi (East)",
        "district_np": "नवलपरासी (बर्दघाट सुस्ता पूर्व)"
      }
    },
    {
      "id": 447,
      "lgid": 40806,
      
      "lgname_en": "Kawasoti Municipality",
      "lgname_np": "कावासोती नगरपालिका",
      "province": {
        "id": 4,
        "province_en": "Gandaki Province",
        "province_np": "गण्डकी प्रदेश",
        
      },
      "district": {
        "id": 43,
        "did": 408,
        
        "district_en": "Nawalparasi (East)",
        "district_np": "नवलपरासी (बर्दघाट सुस्ता पूर्व)"
      }
    },
    {
      "id": 448,
      "lgid": 40807,
      
      "lgname_en": "Madhyabindu Municipality",
      "lgname_np": "मध्यविन्दु नगरपालिका",
      "province": {
        "id": 4,
        "province_en": "Gandaki Province",
        "province_np": "गण्डकी प्रदेश",
        
      },
      "district": {
        "id": 43,
        "did": 408,
        
        "district_en": "Nawalparasi (East)",
        "district_np": "नवलपरासी (बर्दघाट सुस्ता पूर्व)"
      }
    },
    {
      "id": 449,
      "lgid": 40808,
      
      "lgname_en": "Binayitribeni Rural Mun",
      "lgname_np": "विनयी त्रिवेणी गाउँपालिका",
      "province": {
        "id": 4,
        "province_en": "Gandaki Province",
        "province_np": "गण्डकी प्रदेश",
        
      },
      "district": {
        "id": 43,
        "did": 408,
        
        "district_en": "Nawalparasi (East)",
        "district_np": "नवलपरासी (बर्दघाट सुस्ता पूर्व)"
      }
    },
    {
      "id": 450,
      "lgid": 40901,
      
      "lgname_en": "Putalibazar Municipality",
      "lgname_np": "पुतलीबजार नगरपालिका ",
      "province": {
        "id": 4,
        "province_en": "Gandaki Province",
        "province_np": "गण्डकी प्रदेश",
        
      },
      "district": {
        "id": 44,
        "did": 409,
        
        "district_en": "Syangja",
        "district_np": "स्याङजा"
      }
    },
    {
      "id": 451,
      "lgid": 40902,
      
      "lgname_en": "Phedikhola Rural Mun",
      "lgname_np": "फेदीखोला गाउँपालिका ",
      "province": {
        "id": 4,
        "province_en": "Gandaki Province",
        "province_np": "गण्डकी प्रदेश",
        
      },
      "district": {
        "id": 44,
        "did": 409,
        
        "district_en": "Syangja",
        "district_np": "स्याङजा"
      }
    },
    {
      "id": 452,
      "lgid": 40903,
      
      "lgname_en": "Aandhikhola Rural Mun",
      "lgname_np": "आँधिखोला गाउँपालिका ",
      "province": {
        "id": 4,
        "province_en": "Gandaki Province",
        "province_np": "गण्डकी प्रदेश",
        
      },
      "district": {
        "id": 44,
        "did": 409,
        
        "district_en": "Syangja",
        "district_np": "स्याङजा"
      }
    },
    {
      "id": 453,
      "lgid": 40904,
      
      "lgname_en": "Arjunchaupari Rural Mun",
      "lgname_np": "अर्जुनचौपारी गाउँपालिका ",
      "province": {
        "id": 4,
        "province_en": "Gandaki Province",
        "province_np": "गण्डकी प्रदेश",
        
      },
      "district": {
        "id": 44,
        "did": 409,
        
        "district_en": "Syangja",
        "district_np": "स्याङजा"
      }
    },
    {
      "id": 454,
      "lgid": 40905,
      
      "lgname_en": "Bheerkot Municipality",
      "lgname_np": "भीरकोट नगरपालिका ",
      "province": {
        "id": 4,
        "province_en": "Gandaki Province",
        "province_np": "गण्डकी प्रदेश",
        
      },
      "district": {
        "id": 44,
        "did": 409,
        
        "district_en": "Syangja",
        "district_np": "स्याङजा"
      }
    },
    {
      "id": 455,
      "lgid": 40906,
      
      "lgname_en": "Biruwa Rural Mun",
      "lgname_np": "बिरुवा गाउँपालिका ",
      "province": {
        "id": 4,
        "province_en": "Gandaki Province",
        "province_np": "गण्डकी प्रदेश",
        
      },
      "district": {
        "id": 44,
        "did": 409,
        
        "district_en": "Syangja",
        "district_np": "स्याङजा"
      }
    },
    {
      "id": 456,
      "lgid": 40907,
      
      "lgname_en": "Harinas Rural Mun",
      "lgname_np": "हरिनास गाउँपालिका ",
      "province": {
        "id": 4,
        "province_en": "Gandaki Province",
        "province_np": "गण्डकी प्रदेश",
        
      },
      "district": {
        "id": 44,
        "did": 409,
        
        "district_en": "Syangja",
        "district_np": "स्याङजा"
      }
    },
    {
      "id": 457,
      "lgid": 40908,
      
      "lgname_en": "Chapakot Municipality",
      "lgname_np": "चापाकोट नगरपालिका",
      "province": {
        "id": 4,
        "province_en": "Gandaki Province",
        "province_np": "गण्डकी प्रदेश",
        
      },
      "district": {
        "id": 44,
        "did": 409,
        
        "district_en": "Syangja",
        "district_np": "स्याङजा"
      }
    },
    {
      "id": 458,
      "lgid": 40909,
      
      "lgname_en": "Waling Municipality",
      "lgname_np": "वालिङ नगरपालिका ",
      "province": {
        "id": 4,
        "province_en": "Gandaki Province",
        "province_np": "गण्डकी प्रदेश",
        
      },
      "district": {
        "id": 44,
        "did": 409,
        
        "district_en": "Syangja",
        "district_np": "स्याङजा"
      }
    },
    {
      "id": 459,
      "lgid": 40910,
      
      "lgname_en": "Galyang Municipality",
      "lgname_np": "गल्याङ नगरपालिका",
      "province": {
        "id": 4,
        "province_en": "Gandaki Province",
        "province_np": "गण्डकी प्रदेश",
        
      },
      "district": {
        "id": 44,
        "did": 409,
        
        "district_en": "Syangja",
        "district_np": "स्याङजा"
      }
    },
    {
      "id": 460,
      "lgid": 40911,
      
      "lgname_en": "Kaligandaki Rural Mun",
      "lgname_np": "कालीगण्डकी गाउँपालिका ",
      "province": {
        "id": 4,
        "province_en": "Gandaki Province",
        "province_np": "गण्डकी प्रदेश",
        
      },
      "district": {
        "id": 44,
        "did": 409,
        
        "district_en": "Syangja",
        "district_np": "स्याङजा"
      }
    },
    {
      "id": 461,
      "lgid": 41001,
      
      "lgname_en": "Modi Rural Mun",
      "lgname_np": "मोदी गाउँपालिका",
      "province": {
        "id": 4,
        "province_en": "Gandaki Province",
        "province_np": "गण्डकी प्रदेश",
        
      },
      "district": {
        "id": 45,
        "did": 410,
        
        "district_en": "Parbat",
        "district_np": "पर्वत"
      }
    },
    {
      "id": 462,
      "lgid": 41002,
      
      "lgname_en": "Jaljala Rural Mun",
      "lgname_np": "जलजला गाउँपालिका",
      "province": {
        "id": 4,
        "province_en": "Gandaki Province",
        "province_np": "गण्डकी प्रदेश",
        
      },
      "district": {
        "id": 45,
        "did": 410,
        
        "district_en": "Parbat",
        "district_np": "पर्वत"
      }
    },
    {
      "id": 463,
      "lgid": 41003,
      
      "lgname_en": "Kushma Municipality",
      "lgname_np": "कुश्मा नगरपालिका",
      "province": {
        "id": 4,
        "province_en": "Gandaki Province",
        "province_np": "गण्डकी प्रदेश",
        
      },
      "district": {
        "id": 45,
        "did": 410,
        
        "district_en": "Parbat",
        "district_np": "पर्वत"
      }
    },
    {
      "id": 464,
      "lgid": 41004,
      
      "lgname_en": "Phalewas Municipality",
      "lgname_np": "फलेवास नगरपालिका",
      "province": {
        "id": 4,
        "province_en": "Gandaki Province",
        "province_np": "गण्डकी प्रदेश",
        
      },
      "district": {
        "id": 45,
        "did": 410,
        
        "district_en": "Parbat",
        "district_np": "पर्वत"
      }
    },
    {
      "id": 465,
      "lgid": 41005,
      
      "lgname_en": "Mahashila Rural Mun",
      "lgname_np": "महाशिला गाउँपालिका",
      "province": {
        "id": 4,
        "province_en": "Gandaki Province",
        "province_np": "गण्डकी प्रदेश",
        
      },
      "district": {
        "id": 45,
        "did": 410,
        
        "district_en": "Parbat",
        "district_np": "पर्वत"
      }
    },
    {
      "id": 466,
      "lgid": 41006,
      
      "lgname_en": "Bihadi Rural Mun",
      "lgname_np": "विहादी गाउँपालिका",
      "province": {
        "id": 4,
        "province_en": "Gandaki Province",
        "province_np": "गण्डकी प्रदेश",
        
      },
      "district": {
        "id": 45,
        "did": 410,
        
        "district_en": "Parbat",
        "district_np": "पर्वत"
      }
    },
    {
      "id": 467,
      "lgid": 41007,
      
      "lgname_en": "Paiyun Rural Mun",
      "lgname_np": "पैयूं गाउँपालिका",
      "province": {
        "id": 4,
        "province_en": "Gandaki Province",
        "province_np": "गण्डकी प्रदेश",
        
      },
      "district": {
        "id": 45,
        "did": 410,
        
        "district_en": "Parbat",
        "district_np": "पर्वत"
      }
    },
    {
      "id": 468,
      "lgid": 41101,
      
      "lgname_en": "Baglung Municipality",
      "lgname_np": "बागलुङ नगरपालिका",
      "province": {
        "id": 4,
        "province_en": "Gandaki Province",
        "province_np": "गण्डकी प्रदेश",
        
      },
      "district": {
        "id": 46,
        "did": 411,
        
        "district_en": "Baglung",
        "district_np": "वाग्लुङ"
      }
    },
    {
      "id": 469,
      "lgid": 41102,
      
      "lgname_en": "Kathekhola Rural Mun",
      "lgname_np": "काठेखोला गाउँपालिका",
      "province": {
        "id": 4,
        "province_en": "Gandaki Province",
        "province_np": "गण्डकी प्रदेश",
        
      },
      "district": {
        "id": 46,
        "did": 411,
        
        "district_en": "Baglung",
        "district_np": "वाग्लुङ"
      }
    },
    {
      "id": 470,
      "lgid": 41103,
      
      "lgname_en": "Tarakhola Rural Mun",
      "lgname_np": "ताराखोला गाउँपालिका",
      "province": {
        "id": 4,
        "province_en": "Gandaki Province",
        "province_np": "गण्डकी प्रदेश",
        
      },
      "district": {
        "id": 46,
        "did": 411,
        
        "district_en": "Baglung",
        "district_np": "वाग्लुङ"
      }
    },
    {
      "id": 471,
      "lgid": 41104,
      
      "lgname_en": "Tamankhola Rural Mun",
      "lgname_np": "तमानखोला गाउँपालिका",
      "province": {
        "id": 4,
        "province_en": "Gandaki Province",
        "province_np": "गण्डकी प्रदेश",
        
      },
      "district": {
        "id": 46,
        "did": 411,
        
        "district_en": "Baglung",
        "district_np": "वाग्लुङ"
      }
    },
    {
      "id": 472,
      "lgid": 41105,
      
      "lgname_en": "Dhorpatan Municipality",
      "lgname_np": "ढोरपाटन नगरपालिका",
      "province": {
        "id": 4,
        "province_en": "Gandaki Province",
        "province_np": "गण्डकी प्रदेश",
        
      },
      "district": {
        "id": 46,
        "did": 411,
        
        "district_en": "Baglung",
        "district_np": "वाग्लुङ"
      }
    },
    {
      "id": 473,
      "lgid": 41106,
      
      "lgname_en": "Nisikhola Rural Mun",
      "lgname_np": "निसीखोला गाउँपालिका",
      "province": {
        "id": 4,
        "province_en": "Gandaki Province",
        "province_np": "गण्डकी प्रदेश",
        
      },
      "district": {
        "id": 46,
        "did": 411,
        
        "district_en": "Baglung",
        "district_np": "वाग्लुङ"
      }
    },
    {
      "id": 474,
      "lgid": 41107,
      
      "lgname_en": "Badigad Rural Mun",
      "lgname_np": "वडिगाड गाउँपालिका",
      "province": {
        "id": 4,
        "province_en": "Gandaki Province",
        "province_np": "गण्डकी प्रदेश",
        
      },
      "district": {
        "id": 46,
        "did": 411,
        
        "district_en": "Baglung",
        "district_np": "वाग्लुङ"
      }
    },
    {
      "id": 475,
      "lgid": 41108,
      
      "lgname_en": "Galkot Municipality",
      "lgname_np": "गल्कोट नगरपालिका",
      "province": {
        "id": 4,
        "province_en": "Gandaki Province",
        "province_np": "गण्डकी प्रदेश",
        
      },
      "district": {
        "id": 46,
        "did": 411,
        
        "district_en": "Baglung",
        "district_np": "वाग्लुङ"
      }
    },
    {
      "id": 476,
      "lgid": 41109,
      
      "lgname_en": "Bareng Rural Mun",
      "lgname_np": "वरेङ गाउँपालिका",
      "province": {
        "id": 4,
        "province_en": "Gandaki Province",
        "province_np": "गण्डकी प्रदेश",
        
      },
      "district": {
        "id": 46,
        "did": 411,
        
        "district_en": "Baglung",
        "district_np": "वाग्लुङ"
      }
    },
    {
      "id": 477,
      "lgid": 41110,
      
      "lgname_en": "Jaimini Municipality",
      "lgname_np": "जैमूनी नगरपालिका",
      "province": {
        "id": 4,
        "province_en": "Gandaki Province",
        "province_np": "गण्डकी प्रदेश",
        
      },
      "district": {
        "id": 46,
        "did": 411,
        
        "district_en": "Baglung",
        "district_np": "वाग्लुङ"
      }
    },
    {
      "id": 478,
      "lgid": 50101,
      
      "lgname_en": "Puthauttarganga Rural Mun",
      "lgname_np": "पुथा उत्तरगंगा गाउँपालिका",
      "province": {
        "id": 5,
        "province_en": "Lumbini Province",
        "province_np": "लुम्बिनी प्रदेश",
        
      },
      "district": {
        "id": 47,
        "did": 501,
        
        "district_en": "Rukum (East)",
        "district_np": "रुकुम (पूर्वी भाग)"
      }
    },
    {
      "id": 479,
      "lgid": 50102,
      
      "lgname_en": "Sisne Rural Mun",
      "lgname_np": "सिस्ने गाउँपालिका",
      "province": {
        "id": 5,
        "province_en": "Lumbini Province",
        "province_np": "लुम्बिनी प्रदेश",
        
      },
      "district": {
        "id": 47,
        "did": 501,
        
        "district_en": "Rukum (East)",
        "district_np": "रुकुम (पूर्वी भाग)"
      }
    },
    {
      "id": 480,
      "lgid": 50103,
      
      "lgname_en": "Bhume Rural Mun",
      "lgname_np": "भूमे गाउँपालिका",
      "province": {
        "id": 5,
        "province_en": "Lumbini Province",
        "province_np": "लुम्बिनी प्रदेश",
        
      },
      "district": {
        "id": 47,
        "did": 501,
        
        "district_en": "Rukum (East)",
        "district_np": "रुकुम (पूर्वी भाग)"
      }
    },
    {
      "id": 481,
      "lgid": 50201,
      
      "lgname_en": "Sunchhahari Rural Mun",
      "lgname_np": "सुनछहरी गाउँपालिका",
      "province": {
        "id": 5,
        "province_en": "Lumbini Province",
        "province_np": "लुम्बिनी प्रदेश",
        
      },
      "district": {
        "id": 48,
        "did": 502,
        
        "district_en": "Rolpa",
        "district_np": "रोल्पा"
      }
    },
    {
      "id": 482,
      "lgid": 50202,
      
      "lgname_en": "Thabang Rural Mun",
      "lgname_np": "थवाङ गाउँपालिका",
      "province": {
        "id": 5,
        "province_en": "Lumbini Province",
        "province_np": "लुम्बिनी प्रदेश",
        
      },
      "district": {
        "id": 48,
        "did": 502,
        
        "district_en": "Rolpa",
        "district_np": "रोल्पा"
      }
    },
    {
      "id": 483,
      "lgid": 50203,
      
      "lgname_en": "Pariwartan Rural Mun",
      "lgname_np": "परिवर्तन गाउँपालिका",
      "province": {
        "id": 5,
        "province_en": "Lumbini Province",
        "province_np": "लुम्बिनी प्रदेश",
        
      },
      "district": {
        "id": 48,
        "did": 502,
        
        "district_en": "Rolpa",
        "district_np": "रोल्पा"
      }
    },
    {
      "id": 484,
      "lgid": 50204,
      
      "lgname_en": "Gangadev Rural Mun",
      "lgname_np": "गंगादेव गाउँपालिका",
      "province": {
        "id": 5,
        "province_en": "Lumbini Province",
        "province_np": "लुम्बिनी प्रदेश",
        
      },
      "district": {
        "id": 48,
        "did": 502,
        
        "district_en": "Rolpa",
        "district_np": "रोल्पा"
      }
    },
    {
      "id": 485,
      "lgid": 50205,
      
      "lgname_en": "Madi Rural Mun",
      "lgname_np": "माडी गाउँपालिका",
      "province": {
        "id": 5,
        "province_en": "Lumbini Province",
        "province_np": "लुम्बिनी प्रदेश",
        
      },
      "district": {
        "id": 48,
        "did": 502,
        
        "district_en": "Rolpa",
        "district_np": "रोल्पा"
      }
    },
    {
      "id": 486,
      "lgid": 50206,
      
      "lgname_en": "Triveni Rural Mun",
      "lgname_np": "त्रिवेणी गाउँपालिका",
      "province": {
        "id": 5,
        "province_en": "Lumbini Province",
        "province_np": "लुम्बिनी प्रदेश",
        
      },
      "district": {
        "id": 48,
        "did": 502,
        
        "district_en": "Rolpa",
        "district_np": "रोल्पा"
      }
    },
    {
      "id": 487,
      "lgid": 50207,
      
      "lgname_en": "Rolpa Municipality",
      "lgname_np": "रोल्पा नगरपालिका",
      "province": {
        "id": 5,
        "province_en": "Lumbini Province",
        "province_np": "लुम्बिनी प्रदेश",
        
      },
      "district": {
        "id": 48,
        "did": 502,
        
        "district_en": "Rolpa",
        "district_np": "रोल्पा"
      }
    },
    {
      "id": 488,
      "lgid": 50208,
      
      "lgname_en": "Runtigadhi Rural Mun",
      "lgname_np": "रुन्टीगढी गाउँपालिका",
      "province": {
        "id": 5,
        "province_en": "Lumbini Province",
        "province_np": "लुम्बिनी प्रदेश",
        
      },
      "district": {
        "id": 48,
        "did": 502,
        
        "district_en": "Rolpa",
        "district_np": "रोल्पा"
      }
    },
    {
      "id": 489,
      "lgid": 50209,
      
      "lgname_en": "Sunil Smriti Rural Mun",
      "lgname_np": "सुनिल स्मृति गाउँपालिका",
      "province": {
        "id": 5,
        "province_en": "Lumbini Province",
        "province_np": "लुम्बिनी प्रदेश",
        
      },
      "district": {
        "id": 48,
        "did": 502,
        
        "district_en": "Rolpa",
        "district_np": "रोल्पा"
      }
    },
    {
      "id": 490,
      "lgid": 50210,
      
      "lgname_en": "Lungri Rural Mun",
      "lgname_np": "लुङग्री गाउँपालिका",
      "province": {
        "id": 5,
        "province_en": "Lumbini Province",
        "province_np": "लुम्बिनी प्रदेश",
        
      },
      "district": {
        "id": 48,
        "did": 502,
        
        "district_en": "Rolpa",
        "district_np": "रोल्पा"
      }
    },
    {
      "id": 491,
      "lgid": 50301,
      
      "lgname_en": "Gaumukhi Rural Mun",
      "lgname_np": "गौमुखी गाउँपालिका",
      "province": {
        "id": 5,
        "province_en": "Lumbini Province",
        "province_np": "लुम्बिनी प्रदेश",
        
      },
      "district": {
        "id": 49,
        "did": 503,
        
        "district_en": "Pyuthan",
        "district_np": "प्यूठान"
      }
    },
    {
      "id": 492,
      "lgid": 50302,
      
      "lgname_en": "Naubahini Rural Mun",
      "lgname_np": "नौवहिनी गाउँपालिका",
      "province": {
        "id": 5,
        "province_en": "Lumbini Province",
        "province_np": "लुम्बिनी प्रदेश",
        
      },
      "district": {
        "id": 49,
        "did": 503,
        
        "district_en": "Pyuthan",
        "district_np": "प्यूठान"
      }
    },
    {
      "id": 493,
      "lgid": 50303,
      
      "lgname_en": "Jhimruk Rural Mun",
      "lgname_np": "झिमरुक गाउँपालिका",
      "province": {
        "id": 5,
        "province_en": "Lumbini Province",
        "province_np": "लुम्बिनी प्रदेश",
        
      },
      "district": {
        "id": 49,
        "did": 503,
        
        "district_en": "Pyuthan",
        "district_np": "प्यूठान"
      }
    },
    {
      "id": 494,
      "lgid": 50304,
      
      "lgname_en": "Pyuthan Municipality",
      "lgname_np": "प्यूठान नगरपालिका",
      "province": {
        "id": 5,
        "province_en": "Lumbini Province",
        "province_np": "लुम्बिनी प्रदेश",
        
      },
      "district": {
        "id": 49,
        "did": 503,
        
        "district_en": "Pyuthan",
        "district_np": "प्यूठान"
      }
    },
    {
      "id": 495,
      "lgid": 50305,
      
      "lgname_en": "Swargadwari Municipality",
      "lgname_np": "स्वर्गद्वारी नगरपालिका",
      "province": {
        "id": 5,
        "province_en": "Lumbini Province",
        "province_np": "लुम्बिनी प्रदेश",
        
      },
      "district": {
        "id": 49,
        "did": 503,
        
        "district_en": "Pyuthan",
        "district_np": "प्यूठान"
      }
    },
    {
      "id": 496,
      "lgid": 50306,
      
      "lgname_en": "Mandavi Rural Mun",
      "lgname_np": "माण्डवी गाउँपालिका",
      "province": {
        "id": 5,
        "province_en": "Lumbini Province",
        "province_np": "लुम्बिनी प्रदेश",
        
      },
      "district": {
        "id": 49,
        "did": 503,
        
        "district_en": "Pyuthan",
        "district_np": "प्यूठान"
      }
    },
    {
      "id": 497,
      "lgid": 50307,
      
      "lgname_en": "Mallarani Rural Mun",
      "lgname_np": "मल्लरानी गाउँपालिका",
      "province": {
        "id": 5,
        "province_en": "Lumbini Province",
        "province_np": "लुम्बिनी प्रदेश",
        
      },
      "district": {
        "id": 49,
        "did": 503,
        
        "district_en": "Pyuthan",
        "district_np": "प्यूठान"
      }
    },
    {
      "id": 498,
      "lgid": 50308,
      
      "lgname_en": "Airawati Rural Mun",
      "lgname_np": "ऐरावती गाउँपालिका",
      "province": {
        "id": 5,
        "province_en": "Lumbini Province",
        "province_np": "लुम्बिनी प्रदेश",
        
      },
      "district": {
        "id": 49,
        "did": 503,
        
        "district_en": "Pyuthan",
        "district_np": "प्यूठान"
      }
    },
    {
      "id": 499,
      "lgid": 50309,
      
      "lgname_en": "Sarumarani Rural Mun",
      "lgname_np": "सरुमारानी गाउँपालिका",
      "province": {
        "id": 5,
        "province_en": "Lumbini Province",
        "province_np": "लुम्बिनी प्रदेश",
        
      },
      "district": {
        "id": 49,
        "did": 503,
        
        "district_en": "Pyuthan",
        "district_np": "प्यूठान"
      }
    },
    {
      "id": 500,
      "lgid": 50401,
      
      "lgname_en": "Kaligandaki Rural Mun",
      "lgname_np": "कालीगण्डकी गाउँपालिका",
      "province": {
        "id": 5,
        "province_en": "Lumbini Province",
        "province_np": "लुम्बिनी प्रदेश",
        
      },
      "district": {
        "id": 50,
        "did": 504,
        
        "district_en": "Gulmi",
        "district_np": "गुल्मी"
      }
    },
    {
      "id": 501,
      "lgid": 50402,
      
      "lgname_en": "Satyawati Rural Mun",
      "lgname_np": "सत्यवती गाउँपालिका",
      "province": {
        "id": 5,
        "province_en": "Lumbini Province",
        "province_np": "लुम्बिनी प्रदेश",
        
      },
      "district": {
        "id": 50,
        "did": 504,
        
        "district_en": "Gulmi",
        "district_np": "गुल्मी"
      }
    },
    {
      "id": 502,
      "lgid": 50403,
      
      "lgname_en": "Chandrakot Rural Mun",
      "lgname_np": "चन्द्रकोट गाउँपालिका",
      "province": {
        "id": 5,
        "province_en": "Lumbini Province",
        "province_np": "लुम्बिनी प्रदेश",
        
      },
      "district": {
        "id": 50,
        "did": 504,
        
        "district_en": "Gulmi",
        "district_np": "गुल्मी"
      }
    },
    {
      "id": 503,
      "lgid": 50404,
      
      "lgname_en": "Musikot Municipality",
      "lgname_np": "मुसिकोट नगरपालिका",
      "province": {
        "id": 5,
        "province_en": "Lumbini Province",
        "province_np": "लुम्बिनी प्रदेश",
        
      },
      "district": {
        "id": 50,
        "did": 504,
        
        "district_en": "Gulmi",
        "district_np": "गुल्मी"
      }
    },
    {
      "id": 504,
      "lgid": 50405,
      
      "lgname_en": "Ishma Rural Mun",
      "lgname_np": "ईस्मा गाउँपालिका",
      "province": {
        "id": 5,
        "province_en": "Lumbini Province",
        "province_np": "लुम्बिनी प्रदेश",
        
      },
      "district": {
        "id": 50,
        "did": 504,
        
        "district_en": "Gulmi",
        "district_np": "गुल्मी"
      }
    },
    {
      "id": 505,
      "lgid": 50406,
      
      "lgname_en": "Malika Rural Mun",
      "lgname_np": "मालिका गाउँपालिका",
      "province": {
        "id": 5,
        "province_en": "Lumbini Province",
        "province_np": "लुम्बिनी प्रदेश",
        
      },
      "district": {
        "id": 50,
        "did": 504,
        
        "district_en": "Gulmi",
        "district_np": "गुल्मी"
      }
    },
    {
      "id": 506,
      "lgid": 50407,
      
      "lgname_en": "Madane Rural Mun",
      "lgname_np": "मदाने गाउँपालिका",
      "province": {
        "id": 5,
        "province_en": "Lumbini Province",
        "province_np": "लुम्बिनी प्रदेश",
        
      },
      "district": {
        "id": 50,
        "did": 504,
        
        "district_en": "Gulmi",
        "district_np": "गुल्मी"
      }
    },
    {
      "id": 507,
      "lgid": 50408,
      
      "lgname_en": "Dhurkot Rural Mun",
      "lgname_np": "धुर्कोट गाउँपालिका",
      "province": {
        "id": 5,
        "province_en": "Lumbini Province",
        "province_np": "लुम्बिनी प्रदेश",
        
      },
      "district": {
        "id": 50,
        "did": 504,
        
        "district_en": "Gulmi",
        "district_np": "गुल्मी"
      }
    },
    {
      "id": 508,
      "lgid": 50409,
      
      "lgname_en": "Resunga Municipality",
      "lgname_np": "रेसुङ्गा नगरपालिका",
      "province": {
        "id": 5,
        "province_en": "Lumbini Province",
        "province_np": "लुम्बिनी प्रदेश",
        
      },
      "district": {
        "id": 50,
        "did": 504,
        
        "district_en": "Gulmi",
        "district_np": "गुल्मी"
      }
    },
    {
      "id": 509,
      "lgid": 50410,
      
      "lgname_en": "Gulmidarbar Rural Mun",
      "lgname_np": "गुल्मी दरबार गाउँपालिका",
      "province": {
        "id": 5,
        "province_en": "Lumbini Province",
        "province_np": "लुम्बिनी प्रदेश",
        
      },
      "district": {
        "id": 50,
        "did": 504,
        
        "district_en": "Gulmi",
        "district_np": "गुल्मी"
      }
    },
    {
      "id": 510,
      "lgid": 50411,
      
      "lgname_en": "Chhatrakot Rural Mun",
      "lgname_np": "छत्रकोट गाउँपालिका",
      "province": {
        "id": 5,
        "province_en": "Lumbini Province",
        "province_np": "लुम्बिनी प्रदेश",
        
      },
      "district": {
        "id": 50,
        "did": 504,
        
        "district_en": "Gulmi",
        "district_np": "गुल्मी"
      }
    },
    {
      "id": 511,
      "lgid": 50412,
      
      "lgname_en": "Rurukshetra Rural Mun",
      "lgname_np": "रुरुक्षेत्र गाउँपालिका",
      "province": {
        "id": 5,
        "province_en": "Lumbini Province",
        "province_np": "लुम्बिनी प्रदेश",
        
      },
      "district": {
        "id": 50,
        "did": 504,
        
        "district_en": "Gulmi",
        "district_np": "गुल्मी"
      }
    },
    {
      "id": 512,
      "lgid": 50501,
      
      "lgname_en": "Chhatradev Rural Mun",
      "lgname_np": "छत्रदेव गाउँपालिका",
      "province": {
        "id": 5,
        "province_en": "Lumbini Province",
        "province_np": "लुम्बिनी प्रदेश",
        
      },
      "district": {
        "id": 51,
        "did": 505,
        
        "district_en": "Arghakhanchi",
        "district_np": "अर्घाखाँची"
      }
    },
    {
      "id": 513,
      "lgid": 50502,
      
      "lgname_en": "Malarani Rural Mun",
      "lgname_np": "मालारानी गाउँपालिका",
      "province": {
        "id": 5,
        "province_en": "Lumbini Province",
        "province_np": "लुम्बिनी प्रदेश",
        
      },
      "district": {
        "id": 51,
        "did": 505,
        
        "district_en": "Arghakhanchi",
        "district_np": "अर्घाखाँची"
      }
    },
    {
      "id": 514,
      "lgid": 50503,
      
      "lgname_en": "Bhumikasthan Municipality",
      "lgname_np": "भूमिकास्थान नगरपालिका",
      "province": {
        "id": 5,
        "province_en": "Lumbini Province",
        "province_np": "लुम्बिनी प्रदेश",
        
      },
      "district": {
        "id": 51,
        "did": 505,
        
        "district_en": "Arghakhanchi",
        "district_np": "अर्घाखाँची"
      }
    },
    {
      "id": 515,
      "lgid": 50504,
      
      "lgname_en": "Sandhikharka Municipality",
      "lgname_np": "सन्धिखर्क नगरपालिका",
      "province": {
        "id": 5,
        "province_en": "Lumbini Province",
        "province_np": "लुम्बिनी प्रदेश",
        
      },
      "district": {
        "id": 51,
        "did": 505,
        
        "district_en": "Arghakhanchi",
        "district_np": "अर्घाखाँची"
      }
    },
    {
      "id": 516,
      "lgid": 50505,
      
      "lgname_en": "Panini Rural Mun",
      "lgname_np": "पाणिनी गाउँपालिका",
      "province": {
        "id": 5,
        "province_en": "Lumbini Province",
        "province_np": "लुम्बिनी प्रदेश",
        
      },
      "district": {
        "id": 51,
        "did": 505,
        
        "district_en": "Arghakhanchi",
        "district_np": "अर्घाखाँची"
      }
    },
    {
      "id": 517,
      "lgid": 50506,
      
      "lgname_en": "Shitaganga Municipality",
      "lgname_np": "शितगंगा नगरपालिका",
      "province": {
        "id": 5,
        "province_en": "Lumbini Province",
        "province_np": "लुम्बिनी प्रदेश",
        
      },
      "district": {
        "id": 51,
        "did": 505,
        
        "district_en": "Arghakhanchi",
        "district_np": "अर्घाखाँची"
      }
    },
    {
      "id": 518,
      "lgid": 50601,
      
      "lgname_en": "Rampur Municipality",
      "lgname_np": "रामपुर नगरपालिका",
      "province": {
        "id": 5,
        "province_en": "Lumbini Province",
        "province_np": "लुम्बिनी प्रदेश",
        
      },
      "district": {
        "id": 52,
        "did": 506,
        
        "district_en": "Palpa",
        "district_np": "पाल्पा"
      }
    },
    {
      "id": 519,
      "lgid": 50602,
      
      "lgname_en": "Purbakhola Rural Mun",
      "lgname_np": "पूर्वखोला गाउँपालिका",
      "province": {
        "id": 5,
        "province_en": "Lumbini Province",
        "province_np": "लुम्बिनी प्रदेश",
        
      },
      "district": {
        "id": 52,
        "did": 506,
        
        "district_en": "Palpa",
        "district_np": "पाल्पा"
      }
    },
    {
      "id": 520,
      "lgid": 50603,
      
      "lgname_en": "Rambha Rural Mun",
      "lgname_np": "रम्भा गाउँपालिका",
      "province": {
        "id": 5,
        "province_en": "Lumbini Province",
        "province_np": "लुम्बिनी प्रदेश",
        
      },
      "district": {
        "id": 52,
        "did": 506,
        
        "district_en": "Palpa",
        "district_np": "पाल्पा"
      }
    },
    {
      "id": 521,
      "lgid": 50604,
      
      "lgname_en": "Baganaskali Rural Mun",
      "lgname_np": "बगनासकाली गाउँपालिका",
      "province": {
        "id": 5,
        "province_en": "Lumbini Province",
        "province_np": "लुम्बिनी प्रदेश",
        
      },
      "district": {
        "id": 52,
        "did": 506,
        
        "district_en": "Palpa",
        "district_np": "पाल्पा"
      }
    },
    {
      "id": 522,
      "lgid": 50605,
      
      "lgname_en": "Tansen Municipality",
      "lgname_np": "तानसेन नगरपालिका",
      "province": {
        "id": 5,
        "province_en": "Lumbini Province",
        "province_np": "लुम्बिनी प्रदेश",
        
      },
      "district": {
        "id": 52,
        "did": 506,
        
        "district_en": "Palpa",
        "district_np": "पाल्पा"
      }
    },
    {
      "id": 523,
      "lgid": 50606,
      
      "lgname_en": "Ribdikot Rural Mun",
      "lgname_np": "रिब्दिकोट गाउँपालिका",
      "province": {
        "id": 5,
        "province_en": "Lumbini Province",
        "province_np": "लुम्बिनी प्रदेश",
        
      },
      "district": {
        "id": 52,
        "did": 506,
        
        "district_en": "Palpa",
        "district_np": "पाल्पा"
      }
    },
    {
      "id": 524,
      "lgid": 50607,
      
      "lgname_en": "Rainadevichhahara Rural Mun",
      "lgname_np": "रैनादेवी छहरा गाउँपालिका",
      "province": {
        "id": 5,
        "province_en": "Lumbini Province",
        "province_np": "लुम्बिनी प्रदेश",
        
      },
      "district": {
        "id": 52,
        "did": 506,
        
        "district_en": "Palpa",
        "district_np": "पाल्पा"
      }
    },
    {
      "id": 525,
      "lgid": 50608,
      
      "lgname_en": "Tinau Rural Mun",
      "lgname_np": "तिनाउ गाउँपालिका",
      "province": {
        "id": 5,
        "province_en": "Lumbini Province",
        "province_np": "लुम्बिनी प्रदेश",
        
      },
      "district": {
        "id": 52,
        "did": 506,
        
        "district_en": "Palpa",
        "district_np": "पाल्पा"
      }
    },
    {
      "id": 526,
      "lgid": 50609,
      
      "lgname_en": "Mathagadhi Rural Mun",
      "lgname_np": "माथागढी गाउँपालिका",
      "province": {
        "id": 5,
        "province_en": "Lumbini Province",
        "province_np": "लुम्बिनी प्रदेश",
        
      },
      "district": {
        "id": 52,
        "did": 506,
        
        "district_en": "Palpa",
        "district_np": "पाल्पा"
      }
    },
    {
      "id": 527,
      "lgid": 50610,
      
      "lgname_en": "Nisdi Rural Mun",
      "lgname_np": "निस्दी गाउँपालिका",
      "province": {
        "id": 5,
        "province_en": "Lumbini Province",
        "province_np": "लुम्बिनी प्रदेश",
        
      },
      "district": {
        "id": 52,
        "did": 506,
        
        "district_en": "Palpa",
        "district_np": "पाल्पा"
      }
    },
    {
      "id": 528,
      "lgid": 50701,
      
      "lgname_en": "Bardghat Municipality",
      "lgname_np": "बर्दघाट नगरपालिका",
      "province": {
        "id": 5,
        "province_en": "Lumbini Province",
        "province_np": "लुम्बिनी प्रदेश",
        
      },
      "district": {
        "id": 53,
        "did": 507,
        
        "district_en": "Nawalparasi (West)",
        "district_np": "नवलपरासी (बर्दघाट सुस्ता पश्चिम)"
      }
    },
    {
      "id": 529,
      "lgid": 50702,
      
      "lgname_en": "Sunwal Municipality",
      "lgname_np": "सुनवल नगरपालिका",
      "province": {
        "id": 5,
        "province_en": "Lumbini Province",
        "province_np": "लुम्बिनी प्रदेश",
        
      },
      "district": {
        "id": 53,
        "did": 507,
        
        "district_en": "Nawalparasi (West)",
        "district_np": "नवलपरासी (बर्दघाट सुस्ता पश्चिम)"
      }
    },
    {
      "id": 530,
      "lgid": 50703,
      
      "lgname_en": "Ramgram Municipality",
      "lgname_np": "रामग्राम नगरपालिका",
      "province": {
        "id": 5,
        "province_en": "Lumbini Province",
        "province_np": "लुम्बिनी प्रदेश",
        
      },
      "district": {
        "id": 53,
        "did": 507,
        
        "district_en": "Nawalparasi (West)",
        "district_np": "नवलपरासी (बर्दघाट सुस्ता पश्चिम)"
      }
    },
    {
      "id": 531,
      "lgid": 50704,
      
      "lgname_en": "Palhinandan Rural Mun",
      "lgname_np": "पाल्हीनन्दन गाउँपालिका",
      "province": {
        "id": 5,
        "province_en": "Lumbini Province",
        "province_np": "लुम्बिनी प्रदेश",
        
      },
      "district": {
        "id": 53,
        "did": 507,
        
        "district_en": "Nawalparasi (West)",
        "district_np": "नवलपरासी (बर्दघाट सुस्ता पश्चिम)"
      }
    },
    {
      "id": 532,
      "lgid": 50705,
      
      "lgname_en": "Sarawal Rural Mun",
      "lgname_np": "सरावल गाउँपालिका",
      "province": {
        "id": 5,
        "province_en": "Lumbini Province",
        "province_np": "लुम्बिनी प्रदेश",
        
      },
      "district": {
        "id": 53,
        "did": 507,
        
        "district_en": "Nawalparasi (West)",
        "district_np": "नवलपरासी (बर्दघाट सुस्ता पश्चिम)"
      }
    },
    {
      "id": 533,
      "lgid": 50706,
      
      "lgname_en": "Pratappur Rural Mun",
      "lgname_np": "प्रतापपुर गाउँपालिका",
      "province": {
        "id": 5,
        "province_en": "Lumbini Province",
        "province_np": "लुम्बिनी प्रदेश",
        
      },
      "district": {
        "id": 53,
        "did": 507,
        
        "district_en": "Nawalparasi (West)",
        "district_np": "नवलपरासी (बर्दघाट सुस्ता पश्चिम)"
      }
    },
    {
      "id": 534,
      "lgid": 50707,
      
      "lgname_en": "Susta Rural Mun",
      "lgname_np": "सुस्ता गाउँपालिका",
      "province": {
        "id": 5,
        "province_en": "Lumbini Province",
        "province_np": "लुम्बिनी प्रदेश",
        
      },
      "district": {
        "id": 53,
        "did": 507,
        
        "district_en": "Nawalparasi (West)",
        "district_np": "नवलपरासी (बर्दघाट सुस्ता पश्चिम)"
      }
    },
    {
      "id": 535,
      "lgid": 50801,
      
      "lgname_en": "Devdaha Municipality",
      "lgname_np": "देवदह नगरपालिका",
      "province": {
        "id": 5,
        "province_en": "Lumbini Province",
        "province_np": "लुम्बिनी प्रदेश",
        
      },
      "district": {
        "id": 54,
        "did": 508,
        
        "district_en": "Rupandehi",
        "district_np": "रुपन्देही"
      }
    },
    {
      "id": 536,
      "lgid": 50802,
      
      "lgname_en": "Butwal Sub-Metro",
      "lgname_np": "बुटवल उपमहानगरपालिका",
      "province": {
        "id": 5,
        "province_en": "Lumbini Province",
        "province_np": "लुम्बिनी प्रदेश",
        
      },
      "district": {
        "id": 54,
        "did": 508,
        
        "district_en": "Rupandehi",
        "district_np": "रुपन्देही"
      }
    },
    {
      "id": 537,
      "lgid": 50803,
      
      "lgname_en": "Sainamaina Municipality",
      "lgname_np": "सैनामैना नगरपालिका",
      "province": {
        "id": 5,
        "province_en": "Lumbini Province",
        "province_np": "लुम्बिनी प्रदेश",
        
      },
      "district": {
        "id": 54,
        "did": 508,
        
        "district_en": "Rupandehi",
        "district_np": "रुपन्देही"
      }
    },
    {
      "id": 538,
      "lgid": 50804,
      
      "lgname_en": "Kanchan Rural Mun",
      "lgname_np": "कन्चन गाउँपालिका",
      "province": {
        "id": 5,
        "province_en": "Lumbini Province",
        "province_np": "लुम्बिनी प्रदेश",
        
      },
      "district": {
        "id": 54,
        "did": 508,
        
        "district_en": "Rupandehi",
        "district_np": "रुपन्देही"
      }
    },
    {
      "id": 539,
      "lgid": 50805,
      
      "lgname_en": "Gaidahawa Rural Mun",
      "lgname_np": "गैडहवा गाउँपालिका",
      "province": {
        "id": 5,
        "province_en": "Lumbini Province",
        "province_np": "लुम्बिनी प्रदेश",
        
      },
      "district": {
        "id": 54,
        "did": 508,
        
        "district_en": "Rupandehi",
        "district_np": "रुपन्देही"
      }
    },
    {
      "id": 540,
      "lgid": 50806,
      
      "lgname_en": "Shuddhodhan Rural Mun",
      "lgname_np": "शुद्धोधन गाउँपालिका",
      "province": {
        "id": 5,
        "province_en": "Lumbini Province",
        "province_np": "लुम्बिनी प्रदेश",
        
      },
      "district": {
        "id": 54,
        "did": 508,
        
        "district_en": "Rupandehi",
        "district_np": "रुपन्देही"
      }
    },
    {
      "id": 541,
      "lgid": 50807,
      
      "lgname_en": "Siyari Rural Mun",
      "lgname_np": "सियारी गाउँपालिका",
      "province": {
        "id": 5,
        "province_en": "Lumbini Province",
        "province_np": "लुम्बिनी प्रदेश",
        
      },
      "district": {
        "id": 54,
        "did": 508,
        
        "district_en": "Rupandehi",
        "district_np": "रुपन्देही"
      }
    },
    {
      "id": 542,
      "lgid": 50808,
      
      "lgname_en": "Tilottama Municipality",
      "lgname_np": "तिलोत्तमा नगरपालिका",
      "province": {
        "id": 5,
        "province_en": "Lumbini Province",
        "province_np": "लुम्बिनी प्रदेश",
        
      },
      "district": {
        "id": 54,
        "did": 508,
        
        "district_en": "Rupandehi",
        "district_np": "रुपन्देही"
      }
    },
    {
      "id": 543,
      "lgid": 50809,
      
      "lgname_en": "Omsatiya Rural Mun",
      "lgname_np": "ओमसतिया गाउँपालिका",
      "province": {
        "id": 5,
        "province_en": "Lumbini Province",
        "province_np": "लुम्बिनी प्रदेश",
        
      },
      "district": {
        "id": 54,
        "did": 508,
        
        "district_en": "Rupandehi",
        "district_np": "रुपन्देही"
      }
    },
    {
      "id": 544,
      "lgid": 50810,
      
      "lgname_en": "Rohini Rural Mun",
      "lgname_np": "रोहिणी गाउँपालिका",
      "province": {
        "id": 5,
        "province_en": "Lumbini Province",
        "province_np": "लुम्बिनी प्रदेश",
        
      },
      "district": {
        "id": 54,
        "did": 508,
        
        "district_en": "Rupandehi",
        "district_np": "रुपन्देही"
      }
    },
    {
      "id": 545,
      "lgid": 50811,
      
      "lgname_en": "Siddharthanagar Municipality",
      "lgname_np": "सिद्धार्थनगर नगरपालिका",
      "province": {
        "id": 5,
        "province_en": "Lumbini Province",
        "province_np": "लुम्बिनी प्रदेश",
        
      },
      "district": {
        "id": 54,
        "did": 508,
        
        "district_en": "Rupandehi",
        "district_np": "रुपन्देही"
      }
    },
    {
      "id": 546,
      "lgid": 50812,
      
      "lgname_en": "Mayadevi Rural Mun",
      "lgname_np": "मायादेवी गाउँपालिका",
      "province": {
        "id": 5,
        "province_en": "Lumbini Province",
        "province_np": "लुम्बिनी प्रदेश",
        
      },
      "district": {
        "id": 54,
        "did": 508,
        
        "district_en": "Rupandehi",
        "district_np": "रुपन्देही"
      }
    },
    {
      "id": 547,
      "lgid": 50813,
      
      "lgname_en": "Lumbinisanskritik Municipality",
      "lgname_np": "लुम्बिनी सांस्कृतिक नगरपालिका",
      "province": {
        "id": 5,
        "province_en": "Lumbini Province",
        "province_np": "लुम्बिनी प्रदेश",
        
      },
      "district": {
        "id": 54,
        "did": 508,
        
        "district_en": "Rupandehi",
        "district_np": "रुपन्देही"
      }
    },
    {
      "id": 548,
      "lgid": 50814,
      
      "lgname_en": "Kotahimai Rural Mun",
      "lgname_np": "कोटहीमाई गाउँपालिका",
      "province": {
        "id": 5,
        "province_en": "Lumbini Province",
        "province_np": "लुम्बिनी प्रदेश",
        
      },
      "district": {
        "id": 54,
        "did": 508,
        
        "district_en": "Rupandehi",
        "district_np": "रुपन्देही"
      }
    },
    {
      "id": 549,
      "lgid": 50815,
      
      "lgname_en": "Sammarimai Rural Mun",
      "lgname_np": "सम्मरीमाई गाउँपालिका",
      "province": {
        "id": 5,
        "province_en": "Lumbini Province",
        "province_np": "लुम्बिनी प्रदेश",
        
      },
      "district": {
        "id": 54,
        "did": 508,
        
        "district_en": "Rupandehi",
        "district_np": "रुपन्देही"
      }
    },
    {
      "id": 550,
      "lgid": 50816,
      
      "lgname_en": "Marchawari Rural Mun",
      "lgname_np": "मर्चवारी गाउँपालिका",
      "province": {
        "id": 5,
        "province_en": "Lumbini Province",
        "province_np": "लुम्बिनी प्रदेश",
        
      },
      "district": {
        "id": 54,
        "did": 508,
        
        "district_en": "Rupandehi",
        "district_np": "रुपन्देही"
      }
    },
    {
      "id": 551,
      "lgid": 50901,
      
      "lgname_en": "Banganga Municipality",
      "lgname_np": "बाणगंगा नगरपालिका",
      "province": {
        "id": 5,
        "province_en": "Lumbini Province",
        "province_np": "लुम्बिनी प्रदेश",
        
      },
      "district": {
        "id": 55,
        "did": 509,
        
        "district_en": "Kapilvastu",
        "district_np": "कपिलबस्तु"
      }
    },
    {
      "id": 552,
      "lgid": 50902,
      
      "lgname_en": "Buddhabhumi Municipality",
      "lgname_np": "बुद्धभुमी नगरपालिका",
      "province": {
        "id": 5,
        "province_en": "Lumbini Province",
        "province_np": "लुम्बिनी प्रदेश",
        
      },
      "district": {
        "id": 55,
        "did": 509,
        
        "district_en": "Kapilvastu",
        "district_np": "कपिलबस्तु"
      }
    },
    {
      "id": 553,
      "lgid": 50903,
      
      "lgname_en": "Shivraj Municipality",
      "lgname_np": "शिवराज नगरपालिका",
      "province": {
        "id": 5,
        "province_en": "Lumbini Province",
        "province_np": "लुम्बिनी प्रदेश",
        
      },
      "district": {
        "id": 55,
        "did": 509,
        
        "district_en": "Kapilvastu",
        "district_np": "कपिलबस्तु"
      }
    },
    {
      "id": 554,
      "lgid": 50904,
      
      "lgname_en": "Bijaynagar Rural Mun",
      "lgname_np": "विजयनगर गाउँपालिका",
      "province": {
        "id": 5,
        "province_en": "Lumbini Province",
        "province_np": "लुम्बिनी प्रदेश",
        
      },
      "district": {
        "id": 55,
        "did": 509,
        
        "district_en": "Kapilvastu",
        "district_np": "कपिलबस्तु"
      }
    },
    {
      "id": 555,
      "lgid": 50905,
      
      "lgname_en": "Krishnanagar Municipality",
      "lgname_np": "कृष्णनगर नगरपालिका",
      "province": {
        "id": 5,
        "province_en": "Lumbini Province",
        "province_np": "लुम्बिनी प्रदेश",
        
      },
      "district": {
        "id": 55,
        "did": 509,
        
        "district_en": "Kapilvastu",
        "district_np": "कपिलबस्तु"
      }
    },
    {
      "id": 556,
      "lgid": 50906,
      
      "lgname_en": "Maharajgunj Municipality",
      "lgname_np": "महाराजगंज नगरपालिका",
      "province": {
        "id": 5,
        "province_en": "Lumbini Province",
        "province_np": "लुम्बिनी प्रदेश",
        
      },
      "district": {
        "id": 55,
        "did": 509,
        
        "district_en": "Kapilvastu",
        "district_np": "कपिलबस्तु"
      }
    },
    {
      "id": 557,
      "lgid": 50907,
      
      "lgname_en": "Kapilvastu Municipality",
      "lgname_np": "कपिलवस्तु नगरपालिका",
      "province": {
        "id": 5,
        "province_en": "Lumbini Province",
        "province_np": "लुम्बिनी प्रदेश",
        
      },
      "district": {
        "id": 55,
        "did": 509,
        
        "district_en": "Kapilvastu",
        "district_np": "कपिलबस्तु"
      }
    },
    {
      "id": 558,
      "lgid": 50908,
      
      "lgname_en": "Yasodhara Rural Mun",
      "lgname_np": "यसोधरा गाउँपालिका",
      "province": {
        "id": 5,
        "province_en": "Lumbini Province",
        "province_np": "लुम्बिनी प्रदेश",
        
      },
      "district": {
        "id": 55,
        "did": 509,
        
        "district_en": "Kapilvastu",
        "district_np": "कपिलबस्तु"
      }
    },
    {
      "id": 559,
      "lgid": 50909,
      
      "lgname_en": "Mayadevi Rural Mun",
      "lgname_np": "मायादेवी गाउँपालिका",
      "province": {
        "id": 5,
        "province_en": "Lumbini Province",
        "province_np": "लुम्बिनी प्रदेश",
        
      },
      "district": {
        "id": 55,
        "did": 509,
        
        "district_en": "Kapilvastu",
        "district_np": "कपिलबस्तु"
      }
    },
    {
      "id": 560,
      "lgid": 50910,
      
      "lgname_en": "Shuddhodhan Rural Mun",
      "lgname_np": "सुद्धोधन गाउँपालिका",
      "province": {
        "id": 5,
        "province_en": "Lumbini Province",
        "province_np": "लुम्बिनी प्रदेश",
        
      },
      "district": {
        "id": 55,
        "did": 509,
        
        "district_en": "Kapilvastu",
        "district_np": "कपिलबस्तु"
      }
    },
    {
      "id": 561,
      "lgid": 51001,
      
      "lgname_en": "Bangalachuli Rural Mun",
      "lgname_np": "बंगलाचुली गाउँपालिका",
      "province": {
        "id": 5,
        "province_en": "Lumbini Province",
        "province_np": "लुम्बिनी प्रदेश",
        
      },
      "district": {
        "id": 56,
        "did": 510,
        
        "district_en": "Dang",
        "district_np": "दाङ"
      }
    },
    {
      "id": 562,
      "lgid": 51002,
      
      "lgname_en": "Ghorahi Sub-Metro",
      "lgname_np": "घोराही उपमहानगरपालिका",
      "province": {
        "id": 5,
        "province_en": "Lumbini Province",
        "province_np": "लुम्बिनी प्रदेश",
        
      },
      "district": {
        "id": 56,
        "did": 510,
        
        "district_en": "Dang",
        "district_np": "दाङ"
      }
    },
    {
      "id": 563,
      "lgid": 51003,
      
      "lgname_en": "Tulsipur Sub-Metro",
      "lgname_np": "तुल्सीपुर उपमहानगरपालिका",
      "province": {
        "id": 5,
        "province_en": "Lumbini Province",
        "province_np": "लुम्बिनी प्रदेश",
        
      },
      "district": {
        "id": 56,
        "did": 510,
        
        "district_en": "Dang",
        "district_np": "दाङ"
      }
    },
    {
      "id": 564,
      "lgid": 51004,
      
      "lgname_en": "Shantinagar Rural Mun",
      "lgname_np": "शान्तिनगर गाउँपालिका",
      "province": {
        "id": 5,
        "province_en": "Lumbini Province",
        "province_np": "लुम्बिनी प्रदेश",
        
      },
      "district": {
        "id": 56,
        "did": 510,
        
        "district_en": "Dang",
        "district_np": "दाङ"
      }
    },
    {
      "id": 565,
      "lgid": 51005,
      
      "lgname_en": "Babai Rural Mun",
      "lgname_np": "बबई गाउँपालिका",
      "province": {
        "id": 5,
        "province_en": "Lumbini Province",
        "province_np": "लुम्बिनी प्रदेश",
        
      },
      "district": {
        "id": 56,
        "did": 510,
        
        "district_en": "Dang",
        "district_np": "दाङ"
      }
    },
    {
      "id": 566,
      "lgid": 51006,
      
      "lgname_en": "Dangisharan Rural Mun",
      "lgname_np": "दंगीशरण गाउँपालिका",
      "province": {
        "id": 5,
        "province_en": "Lumbini Province",
        "province_np": "लुम्बिनी प्रदेश",
        
      },
      "district": {
        "id": 56,
        "did": 510,
        
        "district_en": "Dang",
        "district_np": "दाङ"
      }
    },
    {
      "id": 567,
      "lgid": 51007,
      
      "lgname_en": "Lamahi Municipality",
      "lgname_np": "लमही नगरपालिका",
      "province": {
        "id": 5,
        "province_en": "Lumbini Province",
        "province_np": "लुम्बिनी प्रदेश",
        
      },
      "district": {
        "id": 56,
        "did": 510,
        
        "district_en": "Dang",
        "district_np": "दाङ"
      }
    },
    {
      "id": 568,
      "lgid": 51008,
      
      "lgname_en": "Rapti Rural Mun",
      "lgname_np": "राप्ती गाउँपालिका",
      "province": {
        "id": 5,
        "province_en": "Lumbini Province",
        "province_np": "लुम्बिनी प्रदेश",
        
      },
      "district": {
        "id": 56,
        "did": 510,
        
        "district_en": "Dang",
        "district_np": "दाङ"
      }
    },
    {
      "id": 569,
      "lgid": 51009,
      
      "lgname_en": "Gadhawa Rural Mun",
      "lgname_np": "गढवा गाउँपालिका",
      "province": {
        "id": 5,
        "province_en": "Lumbini Province",
        "province_np": "लुम्बिनी प्रदेश",
        
      },
      "district": {
        "id": 56,
        "did": 510,
        
        "district_en": "Dang",
        "district_np": "दाङ"
      }
    },
    {
      "id": 570,
      "lgid": 51010,
      
      "lgname_en": "Rajpur Rural Mun",
      "lgname_np": "राजपुर गाउँपालिका",
      "province": {
        "id": 5,
        "province_en": "Lumbini Province",
        "province_np": "लुम्बिनी प्रदेश",
        
      },
      "district": {
        "id": 56,
        "did": 510,
        
        "district_en": "Dang",
        "district_np": "दाङ"
      }
    },
    {
      "id": 571,
      "lgid": 51101,
      
      "lgname_en": "Raptisonari Rural Mun",
      "lgname_np": "राप्ती सोनारी गाउँपालिका",
      "province": {
        "id": 5,
        "province_en": "Lumbini Province",
        "province_np": "लुम्बिनी प्रदेश",
        
      },
      "district": {
        "id": 57,
        "did": 511,
        
        "district_en": "Banke",
        "district_np": "बाँके"
      }
    },
    {
      "id": 572,
      "lgid": 51102,
      
      "lgname_en": "Kohalpur Municipality",
      "lgname_np": "कोहलपुर नगरपालिका",
      "province": {
        "id": 5,
        "province_en": "Lumbini Province",
        "province_np": "लुम्बिनी प्रदेश",
        
      },
      "district": {
        "id": 57,
        "did": 511,
        
        "district_en": "Banke",
        "district_np": "बाँके"
      }
    },
    {
      "id": 573,
      "lgid": 51103,
      
      "lgname_en": "Baijanath Rural Mun",
      "lgname_np": "बैजनाथ गाउँपालिका",
      "province": {
        "id": 5,
        "province_en": "Lumbini Province",
        "province_np": "लुम्बिनी प्रदेश",
        
      },
      "district": {
        "id": 57,
        "did": 511,
        
        "district_en": "Banke",
        "district_np": "बाँके"
      }
    },
    {
      "id": 574,
      "lgid": 51104,
      
      "lgname_en": "Khajura Rural Mun",
      "lgname_np": "खजुरा गाउँपालिका",
      "province": {
        "id": 5,
        "province_en": "Lumbini Province",
        "province_np": "लुम्बिनी प्रदेश",
        
      },
      "district": {
        "id": 57,
        "did": 511,
        
        "district_en": "Banke",
        "district_np": "बाँके"
      }
    },
    {
      "id": 575,
      "lgid": 51105,
      
      "lgname_en": "Janaki Rural Mun",
      "lgname_np": "जानकी गाउँपालिका",
      "province": {
        "id": 5,
        "province_en": "Lumbini Province",
        "province_np": "लुम्बिनी प्रदेश",
        
      },
      "district": {
        "id": 57,
        "did": 511,
        
        "district_en": "Banke",
        "district_np": "बाँके"
      }
    },
    {
      "id": 576,
      "lgid": 51106,
      
      "lgname_en": "Nepalgunj Sub-Metro",
      "lgname_np": "नेपालगंज उपमहानगरपालिका",
      "province": {
        "id": 5,
        "province_en": "Lumbini Province",
        "province_np": "लुम्बिनी प्रदेश",
        
      },
      "district": {
        "id": 57,
        "did": 511,
        
        "district_en": "Banke",
        "district_np": "बाँके"
      }
    },
    {
      "id": 577,
      "lgid": 51107,
      
      "lgname_en": "Duduwa Rural Mun",
      "lgname_np": "डुडुवा गाउँपालिका",
      "province": {
        "id": 5,
        "province_en": "Lumbini Province",
        "province_np": "लुम्बिनी प्रदेश",
        
      },
      "district": {
        "id": 57,
        "did": 511,
        
        "district_en": "Banke",
        "district_np": "बाँके"
      }
    },
    {
      "id": 578,
      "lgid": 51108,
      
      "lgname_en": "Narainapur Rural Mun",
      "lgname_np": "नरैनापुर गाउँपालिका",
      "province": {
        "id": 5,
        "province_en": "Lumbini Province",
        "province_np": "लुम्बिनी प्रदेश",
        
      },
      "district": {
        "id": 57,
        "did": 511,
        
        "district_en": "Banke",
        "district_np": "बाँके"
      }
    },
    {
      "id": 579,
      "lgid": 51201,
      
      "lgname_en": "Bansgadhi Municipality",
      "lgname_np": "बाँसगढी नगरपालिका",
      "province": {
        "id": 5,
        "province_en": "Lumbini Province",
        "province_np": "लुम्बिनी प्रदेश",
        
      },
      "district": {
        "id": 58,
        "did": 512,
        
        "district_en": "Bardiya",
        "district_np": "बर्दिया"
      }
    },
    {
      "id": 580,
      "lgid": 51202,
      
      "lgname_en": "Barbardiya Municipality",
      "lgname_np": "बारबर्दिया नगरपालिका",
      "province": {
        "id": 5,
        "province_en": "Lumbini Province",
        "province_np": "लुम्बिनी प्रदेश",
        
      },
      "district": {
        "id": 58,
        "did": 512,
        
        "district_en": "Bardiya",
        "district_np": "बर्दिया"
      }
    },
    {
      "id": 581,
      "lgid": 51203,
      
      "lgname_en": "Thakurbaba Municipality",
      "lgname_np": "ठाकुरबाबा नगरपालिका",
      "province": {
        "id": 5,
        "province_en": "Lumbini Province",
        "province_np": "लुम्बिनी प्रदेश",
        
      },
      "district": {
        "id": 58,
        "did": 512,
        
        "district_en": "Bardiya",
        "district_np": "बर्दिया"
      }
    },
    {
      "id": 582,
      "lgid": 51204,
      
      "lgname_en": "Geruwa Rural Mun",
      "lgname_np": "गेरुवा गाउँपालिका",
      "province": {
        "id": 5,
        "province_en": "Lumbini Province",
        "province_np": "लुम्बिनी प्रदेश",
        
      },
      "district": {
        "id": 58,
        "did": 512,
        
        "district_en": "Bardiya",
        "district_np": "बर्दिया"
      }
    },
    {
      "id": 583,
      "lgid": 51205,
      
      "lgname_en": "Rajapur Municipality",
      "lgname_np": "राजापुर नगरपालिका",
      "province": {
        "id": 5,
        "province_en": "Lumbini Province",
        "province_np": "लुम्बिनी प्रदेश",
        
      },
      "district": {
        "id": 58,
        "did": 512,
        
        "district_en": "Bardiya",
        "district_np": "बर्दिया"
      }
    },
    {
      "id": 584,
      "lgid": 51206,
      
      "lgname_en": "Madhuwan Municipality",
      "lgname_np": "मधुवन नगरपालिका",
      "province": {
        "id": 5,
        "province_en": "Lumbini Province",
        "province_np": "लुम्बिनी प्रदेश",
        
      },
      "district": {
        "id": 58,
        "did": 512,
        
        "district_en": "Bardiya",
        "district_np": "बर्दिया"
      }
    },
    {
      "id": 585,
      "lgid": 51207,
      
      "lgname_en": "Gulariya Municipality",
      "lgname_np": "गुलरिया नगरपालिका",
      "province": {
        "id": 5,
        "province_en": "Lumbini Province",
        "province_np": "लुम्बिनी प्रदेश",
        
      },
      "district": {
        "id": 58,
        "did": 512,
        
        "district_en": "Bardiya",
        "district_np": "बर्दिया"
      }
    },
    {
      "id": 586,
      "lgid": 51208,
      
      "lgname_en": "Badhaiyatal Rural Mun",
      "lgname_np": "बढैयाताल गाउँपालिका",
      "province": {
        "id": 5,
        "province_en": "Lumbini Province",
        "province_np": "लुम्बिनी प्रदेश",
        
      },
      "district": {
        "id": 58,
        "did": 512,
        
        "district_en": "Bardiya",
        "district_np": "बर्दिया"
      }
    },
    {
      "id": 587,
      "lgid": 60101,
      
      "lgname_en": "Dolpobuddha Rural Mun",
      "lgname_np": "डोल्पो बुद्ध गाउँपालिका",
      "province": {
        "id": 6,
        "province_en": "Karnali Province",
        "province_np": "कर्णाली प्रदेश",
        
      },
      "district": {
        "id": 59,
        "did": 601,
        
        "district_en": "Dolpa",
        "district_np": "डोल्पा"
      }
    },
    {
      "id": 588,
      "lgid": 60102,
      
      "lgname_en": "Shephoksundo Rural Mun",
      "lgname_np": "शे फोक्सुन्डो गाउँपालिका",
      "province": {
        "id": 6,
        "province_en": "Karnali Province",
        "province_np": "कर्णाली प्रदेश",
        
      },
      "district": {
        "id": 59,
        "did": 601,
        
        "district_en": "Dolpa",
        "district_np": "डोल्पा"
      }
    },
    {
      "id": 589,
      "lgid": 60103,
      
      "lgname_en": "Jagdulla Rural Mun",
      "lgname_np": "जगदुल्ला गाउँपालिका",
      "province": {
        "id": 6,
        "province_en": "Karnali Province",
        "province_np": "कर्णाली प्रदेश",
        
      },
      "district": {
        "id": 59,
        "did": 601,
        
        "district_en": "Dolpa",
        "district_np": "डोल्पा"
      }
    },
    {
      "id": 590,
      "lgid": 60104,
      
      "lgname_en": "Mudkechula Rural Mun",
      "lgname_np": "मुड्केचुला गाउँपालिका",
      "province": {
        "id": 6,
        "province_en": "Karnali Province",
        "province_np": "कर्णाली प्रदेश",
        
      },
      "district": {
        "id": 59,
        "did": 601,
        
        "district_en": "Dolpa",
        "district_np": "डोल्पा"
      }
    },
    {
      "id": 591,
      "lgid": 60105,
      
      "lgname_en": "Tripurasundari Municipality",
      "lgname_np": "त्रिपुरासुन्दरी नगरपालिका",
      "province": {
        "id": 6,
        "province_en": "Karnali Province",
        "province_np": "कर्णाली प्रदेश",
        
      },
      "district": {
        "id": 59,
        "did": 601,
        
        "district_en": "Dolpa",
        "district_np": "डोल्पा"
      }
    },
    {
      "id": 592,
      "lgid": 60106,
      
      "lgname_en": "Thulibheri Municipality",
      "lgname_np": "ठूली भेरी नगरपालिका",
      "province": {
        "id": 6,
        "province_en": "Karnali Province",
        "province_np": "कर्णाली प्रदेश",
        
      },
      "district": {
        "id": 59,
        "did": 601,
        
        "district_en": "Dolpa",
        "district_np": "डोल्पा"
      }
    },
    {
      "id": 593,
      "lgid": 60107,
      
      "lgname_en": "Kaike Rural Mun",
      "lgname_np": "काईके गाउँपालिका",
      "province": {
        "id": 6,
        "province_en": "Karnali Province",
        "province_np": "कर्णाली प्रदेश",
        
      },
      "district": {
        "id": 59,
        "did": 601,
        
        "district_en": "Dolpa",
        "district_np": "डोल्पा"
      }
    },
    {
      "id": 594,
      "lgid": 60108,
      
      "lgname_en": "Chharkatangsong Rural Mun",
      "lgname_np": "छार्का ताङसोङ गाउँपालिका",
      "province": {
        "id": 6,
        "province_en": "Karnali Province",
        "province_np": "कर्णाली प्रदेश",
        
      },
      "district": {
        "id": 59,
        "did": 601,
        
        "district_en": "Dolpa",
        "district_np": "डोल्पा"
      }
    },
    {
      "id": 595,
      "lgid": 60201,
      
      "lgname_en": "Mugumkarmarong Rural Mun",
      "lgname_np": "मुगुम कार्मारोंग गाउँपालिका",
      "province": {
        "id": 6,
        "province_en": "Karnali Province",
        "province_np": "कर्णाली प्रदेश",
        
      },
      "district": {
        "id": 60,
        "did": 602,
        
        "district_en": "Mugu",
        "district_np": "मुगु"
      }
    },
    {
      "id": 596,
      "lgid": 60202,
      
      "lgname_en": "Chhayanathrara Municipality",
      "lgname_np": "छायाँनाथ रारा नगरपालिका",
      "province": {
        "id": 6,
        "province_en": "Karnali Province",
        "province_np": "कर्णाली प्रदेश",
        
      },
      "district": {
        "id": 60,
        "did": 602,
        
        "district_en": "Mugu",
        "district_np": "मुगु"
      }
    },
    {
      "id": 597,
      "lgid": 60203,
      
      "lgname_en": "Soru Rural Mun",
      "lgname_np": "सोरु गाउँपालिका",
      "province": {
        "id": 6,
        "province_en": "Karnali Province",
        "province_np": "कर्णाली प्रदेश",
        
      },
      "district": {
        "id": 60,
        "did": 602,
        
        "district_en": "Mugu",
        "district_np": "मुगु"
      }
    },
    {
      "id": 598,
      "lgid": 60204,
      
      "lgname_en": "Khatyad Rural Mun",
      "lgname_np": "खत्याड गाउँपालिका",
      "province": {
        "id": 6,
        "province_en": "Karnali Province",
        "province_np": "कर्णाली प्रदेश",
        
      },
      "district": {
        "id": 60,
        "did": 602,
        
        "district_en": "Mugu",
        "district_np": "मुगु"
      }
    },
    {
      "id": 599,
      "lgid": 60301,
      
      "lgname_en": "Chankheli Rural Mun",
      "lgname_np": "चंखेली गाउँपालिका",
      "province": {
        "id": 6,
        "province_en": "Karnali Province",
        "province_np": "कर्णाली प्रदेश",
        
      },
      "district": {
        "id": 61,
        "did": 603,
        
        "district_en": "Humla",
        "district_np": "हुम्ला"
      }
    },
    {
      "id": 600,
      "lgid": 60302,
      
      "lgname_en": "Kharpunath Rural Mun",
      "lgname_np": "खार्पुनाथ गाउँपालिका",
      "province": {
        "id": 6,
        "province_en": "Karnali Province",
        "province_np": "कर्णाली प्रदेश",
        
      },
      "district": {
        "id": 61,
        "did": 603,
        
        "district_en": "Humla",
        "district_np": "हुम्ला"
      }
    },
    {
      "id": 601,
      "lgid": 60303,
      
      "lgname_en": "Simkot Rural Mun",
      "lgname_np": "सिमकोट गाउँपालिका",
      "province": {
        "id": 6,
        "province_en": "Karnali Province",
        "province_np": "कर्णाली प्रदेश",
        
      },
      "district": {
        "id": 61,
        "did": 603,
        
        "district_en": "Humla",
        "district_np": "हुम्ला"
      }
    },
    {
      "id": 602,
      "lgid": 60304,
      
      "lgname_en": "Namkha Rural Mun",
      "lgname_np": "नाम्खा गाउँपालिका",
      "province": {
        "id": 6,
        "province_en": "Karnali Province",
        "province_np": "कर्णाली प्रदेश",
        
      },
      "district": {
        "id": 61,
        "did": 603,
        
        "district_en": "Humla",
        "district_np": "हुम्ला"
      }
    },
    {
      "id": 603,
      "lgid": 60305,
      
      "lgname_en": "Sarkegad Rural Mun",
      "lgname_np": "सर्केगाड गाउँपालिका",
      "province": {
        "id": 6,
        "province_en": "Karnali Province",
        "province_np": "कर्णाली प्रदेश",
        
      },
      "district": {
        "id": 61,
        "did": 603,
        
        "district_en": "Humla",
        "district_np": "हुम्ला"
      }
    },
    {
      "id": 604,
      "lgid": 60306,
      
      "lgname_en": "Adanchuli Rural Mun",
      "lgname_np": "अदानचुली गाउँपालिका",
      "province": {
        "id": 6,
        "province_en": "Karnali Province",
        "province_np": "कर्णाली प्रदेश",
        
      },
      "district": {
        "id": 61,
        "did": 603,
        
        "district_en": "Humla",
        "district_np": "हुम्ला"
      }
    },
    {
      "id": 605,
      "lgid": 60307,
      
      "lgname_en": "Tajakot Rural Mun",
      "lgname_np": "ताँजाकोट गाउँपालिका",
      "province": {
        "id": 6,
        "province_en": "Karnali Province",
        "province_np": "कर्णाली प्रदेश",
        
      },
      "district": {
        "id": 61,
        "did": 603,
        
        "district_en": "Humla",
        "district_np": "हुम्ला"
      }
    },
    {
      "id": 606,
      "lgid": 60401,
      
      "lgname_en": "Patarasi Rural Mun",
      "lgname_np": "पातारासी गाउँपालिका",
      "province": {
        "id": 6,
        "province_en": "Karnali Province",
        "province_np": "कर्णाली प्रदेश",
        
      },
      "district": {
        "id": 62,
        "did": 604,
        
        "district_en": "Jumla",
        "district_np": "जुम्ला"
      }
    },
    {
      "id": 607,
      "lgid": 60402,
      
      "lgname_en": "Kankasundari Rural Mun",
      "lgname_np": "कनकासुन्दरी गाउँपालिका",
      "province": {
        "id": 6,
        "province_en": "Karnali Province",
        "province_np": "कर्णाली प्रदेश",
        
      },
      "district": {
        "id": 62,
        "did": 604,
        
        "district_en": "Jumla",
        "district_np": "जुम्ला"
      }
    },
    {
      "id": 608,
      "lgid": 60403,
      
      "lgname_en": "Sinja Rural Mun",
      "lgname_np": "सिंजा गाउँपालिका",
      "province": {
        "id": 6,
        "province_en": "Karnali Province",
        "province_np": "कर्णाली प्रदेश",
        
      },
      "district": {
        "id": 62,
        "did": 604,
        
        "district_en": "Jumla",
        "district_np": "जुम्ला"
      }
    },
    {
      "id": 609,
      "lgid": 60404,
      
      "lgname_en": "Chandannath Municipality",
      "lgname_np": "चन्दननाथ नगरपालिका",
      "province": {
        "id": 6,
        "province_en": "Karnali Province",
        "province_np": "कर्णाली प्रदेश",
        
      },
      "district": {
        "id": 62,
        "did": 604,
        
        "district_en": "Jumla",
        "district_np": "जुम्ला"
      }
    },
    {
      "id": 610,
      "lgid": 60405,
      
      "lgname_en": "Guthichaur Rural Mun",
      "lgname_np": "गुठिचौर गाउँपालिका",
      "province": {
        "id": 6,
        "province_en": "Karnali Province",
        "province_np": "कर्णाली प्रदेश",
        
      },
      "district": {
        "id": 62,
        "did": 604,
        
        "district_en": "Jumla",
        "district_np": "जुम्ला"
      }
    },
    {
      "id": 611,
      "lgid": 60406,
      
      "lgname_en": "Tatopani Rural Mun",
      "lgname_np": "तातोपानी गाउँपालिका",
      "province": {
        "id": 6,
        "province_en": "Karnali Province",
        "province_np": "कर्णाली प्रदेश",
        
      },
      "district": {
        "id": 62,
        "did": 604,
        
        "district_en": "Jumla",
        "district_np": "जुम्ला"
      }
    },
    {
      "id": 612,
      "lgid": 60407,
      
      "lgname_en": "Tila Rural Mun",
      "lgname_np": "तिला गाउँपालिका",
      "province": {
        "id": 6,
        "province_en": "Karnali Province",
        "province_np": "कर्णाली प्रदेश",
        
      },
      "district": {
        "id": 62,
        "did": 604,
        
        "district_en": "Jumla",
        "district_np": "जुम्ला"
      }
    },
    {
      "id": 613,
      "lgid": 60408,
      
      "lgname_en": "Hima Rural Mun",
      "lgname_np": "हिमा गाउँपालिका",
      "province": {
        "id": 6,
        "province_en": "Karnali Province",
        "province_np": "कर्णाली प्रदेश",
        
      },
      "district": {
        "id": 62,
        "did": 604,
        
        "district_en": "Jumla",
        "district_np": "जुम्ला"
      }
    },
    {
      "id": 614,
      "lgid": 60501,
      
      "lgname_en": "Palata Rural Mun",
      "lgname_np": "पलाता गाउँपालिका",
      "province": {
        "id": 6,
        "province_en": "Karnali Province",
        "province_np": "कर्णाली प्रदेश",
        
      },
      "district": {
        "id": 63,
        "did": 605,
        
        "district_en": "Kalikot",
        "district_np": "कालिकोट"
      }
    },
    {
      "id": 615,
      "lgid": 60502,
      
      "lgname_en": "Pachaljharana Rural Mun",
      "lgname_np": "पचालझरना गाउँपालिका",
      "province": {
        "id": 6,
        "province_en": "Karnali Province",
        "province_np": "कर्णाली प्रदेश",
        
      },
      "district": {
        "id": 63,
        "did": 605,
        
        "district_en": "Kalikot",
        "district_np": "कालिकोट"
      }
    },
    {
      "id": 616,
      "lgid": 60503,
      
      "lgname_en": "Raskot Municipality",
      "lgname_np": "रास्कोट नगरपालिका",
      "province": {
        "id": 6,
        "province_en": "Karnali Province",
        "province_np": "कर्णाली प्रदेश",
        
      },
      "district": {
        "id": 63,
        "did": 605,
        
        "district_en": "Kalikot",
        "district_np": "कालिकोट"
      }
    },
    {
      "id": 617,
      "lgid": 60504,
      
      "lgname_en": "Sannitriveni Rural Mun",
      "lgname_np": "सान्नी त्रिवेणी गाउँपालिका",
      "province": {
        "id": 6,
        "province_en": "Karnali Province",
        "province_np": "कर्णाली प्रदेश",
        
      },
      "district": {
        "id": 63,
        "did": 605,
        
        "district_en": "Kalikot",
        "district_np": "कालिकोट"
      }
    },
    {
      "id": 618,
      "lgid": 60505,
      
      "lgname_en": "Narharinath Rural Mun",
      "lgname_np": "नरहरिनाथ गाउँपालिका",
      "province": {
        "id": 6,
        "province_en": "Karnali Province",
        "province_np": "कर्णाली प्रदेश",
        
      },
      "district": {
        "id": 63,
        "did": 605,
        
        "district_en": "Kalikot",
        "district_np": "कालिकोट"
      }
    },
    {
      "id": 619,
      "lgid": 60506,
      
      "lgname_en": "Khandachakra Municipality",
      "lgname_np": "खाँडाचक्र नगरपालिका",
      "province": {
        "id": 6,
        "province_en": "Karnali Province",
        "province_np": "कर्णाली प्रदेश",
        
      },
      "district": {
        "id": 63,
        "did": 605,
        
        "district_en": "Kalikot",
        "district_np": "कालिकोट"
      }
    },
    {
      "id": 620,
      "lgid": 60507,
      
      "lgname_en": "Tilagufa Municipality",
      "lgname_np": "तिलागुफा नगरपालिका",
      "province": {
        "id": 6,
        "province_en": "Karnali Province",
        "province_np": "कर्णाली प्रदेश",
        
      },
      "district": {
        "id": 63,
        "did": 605,
        
        "district_en": "Kalikot",
        "district_np": "कालिकोट"
      }
    },
    {
      "id": 621,
      "lgid": 60508,
      
      "lgname_en": "Mahawai Rural Mun",
      "lgname_np": "महावै गाउँपालिका",
      "province": {
        "id": 6,
        "province_en": "Karnali Province",
        "province_np": "कर्णाली प्रदेश",
        
      },
      "district": {
        "id": 63,
        "did": 605,
        
        "district_en": "Kalikot",
        "district_np": "कालिकोट"
      }
    },
    {
      "id": 622,
      "lgid": 60509,
      
      "lgname_en": "Shuva Kalika Rural Mun",
      "lgname_np": "शुभ कालीका गाउँपालिका",
      "province": {
        "id": 6,
        "province_en": "Karnali Province",
        "province_np": "कर्णाली प्रदेश",
        
      },
      "district": {
        "id": 63,
        "did": 605,
        
        "district_en": "Kalikot",
        "district_np": "कालिकोट"
      }
    },
    {
      "id": 623,
      "lgid": 60601,
      
      "lgname_en": "Naumule Rural Mun",
      "lgname_np": "नौमुले गाउँपालिका",
      "province": {
        "id": 6,
        "province_en": "Karnali Province",
        "province_np": "कर्णाली प्रदेश",
        
      },
      "district": {
        "id": 64,
        "did": 606,
        
        "district_en": "Dailekh",
        "district_np": "दैलेख"
      }
    },
    {
      "id": 624,
      "lgid": 60602,
      
      "lgname_en": "Mahabu Rural Mun",
      "lgname_np": "महावु गाउँपालिका",
      "province": {
        "id": 6,
        "province_en": "Karnali Province",
        "province_np": "कर्णाली प्रदेश",
        
      },
      "district": {
        "id": 64,
        "did": 606,
        
        "district_en": "Dailekh",
        "district_np": "दैलेख"
      }
    },
    {
      "id": 625,
      "lgid": 60603,
      
      "lgname_en": "Bhairabi Rural Mun",
      "lgname_np": "भैरवी गाउँपालिका",
      "province": {
        "id": 6,
        "province_en": "Karnali Province",
        "province_np": "कर्णाली प्रदेश",
        
      },
      "district": {
        "id": 64,
        "did": 606,
        
        "district_en": "Dailekh",
        "district_np": "दैलेख"
      }
    },
    {
      "id": 626,
      "lgid": 60604,
      
      "lgname_en": "Thantikandh Rural Mun",
      "lgname_np": "ठाँटीकाँध गाउँपालिका",
      "province": {
        "id": 6,
        "province_en": "Karnali Province",
        "province_np": "कर्णाली प्रदेश",
        
      },
      "district": {
        "id": 64,
        "did": 606,
        
        "district_en": "Dailekh",
        "district_np": "दैलेख"
      }
    },
    {
      "id": 627,
      "lgid": 60605,
      
      "lgname_en": "Aathabis Municipality",
      "lgname_np": "आठबीस नगरपालिका",
      "province": {
        "id": 6,
        "province_en": "Karnali Province",
        "province_np": "कर्णाली प्रदेश",
        
      },
      "district": {
        "id": 64,
        "did": 606,
        
        "district_en": "Dailekh",
        "district_np": "दैलेख"
      }
    },
    {
      "id": 628,
      "lgid": 60606,
      
      "lgname_en": "Chamundabindrasaini Municipality",
      "lgname_np": "चामुण्डा विन्द्रासैनी नगरपालिका",
      "province": {
        "id": 6,
        "province_en": "Karnali Province",
        "province_np": "कर्णाली प्रदेश",
        
      },
      "district": {
        "id": 64,
        "did": 606,
        
        "district_en": "Dailekh",
        "district_np": "दैलेख"
      }
    },
    {
      "id": 629,
      "lgid": 60607,
      
      "lgname_en": "Dullu Municipality",
      "lgname_np": "दुल्लु नगरपालिका",
      "province": {
        "id": 6,
        "province_en": "Karnali Province",
        "province_np": "कर्णाली प्रदेश",
        
      },
      "district": {
        "id": 64,
        "did": 606,
        
        "district_en": "Dailekh",
        "district_np": "दैलेख"
      }
    },
    {
      "id": 630,
      "lgid": 60608,
      
      "lgname_en": "Narayan Municipality",
      "lgname_np": "नारायण नगरपालिका",
      "province": {
        "id": 6,
        "province_en": "Karnali Province",
        "province_np": "कर्णाली प्रदेश",
        
      },
      "district": {
        "id": 64,
        "did": 606,
        
        "district_en": "Dailekh",
        "district_np": "दैलेख"
      }
    },
    {
      "id": 631,
      "lgid": 60609,
      
      "lgname_en": "Bhagawatimai Rural Mun",
      "lgname_np": "भगवतीमाई गाउँपालिका",
      "province": {
        "id": 6,
        "province_en": "Karnali Province",
        "province_np": "कर्णाली प्रदेश",
        
      },
      "district": {
        "id": 64,
        "did": 606,
        
        "district_en": "Dailekh",
        "district_np": "दैलेख"
      }
    },
    {
      "id": 632,
      "lgid": 60610,
      
      "lgname_en": "Dungeshwor Rural Mun",
      "lgname_np": "डुंगेश्वर गाउँपालिका",
      "province": {
        "id": 6,
        "province_en": "Karnali Province",
        "province_np": "कर्णाली प्रदेश",
        
      },
      "district": {
        "id": 64,
        "did": 606,
        
        "district_en": "Dailekh",
        "district_np": "दैलेख"
      }
    },
    {
      "id": 633,
      "lgid": 60611,
      
      "lgname_en": "Gurans Rural Mun",
      "lgname_np": "गुराँस गाउँपालिका",
      "province": {
        "id": 6,
        "province_en": "Karnali Province",
        "province_np": "कर्णाली प्रदेश",
        
      },
      "district": {
        "id": 64,
        "did": 606,
        
        "district_en": "Dailekh",
        "district_np": "दैलेख"
      }
    },
    {
      "id": 634,
      "lgid": 60701,
      
      "lgname_en": "Barekot Rural Mun",
      "lgname_np": "बारेकोट गाउँपालिका",
      "province": {
        "id": 6,
        "province_en": "Karnali Province",
        "province_np": "कर्णाली प्रदेश",
        
      },
      "district": {
        "id": 65,
        "did": 607,
        
        "district_en": "Jajarkot",
        "district_np": "जाजरकोट"
      }
    },
    {
      "id": 635,
      "lgid": 60702,
      
      "lgname_en": "Kushe Rural Mun",
      "lgname_np": "कुसे गाउँपालिका",
      "province": {
        "id": 6,
        "province_en": "Karnali Province",
        "province_np": "कर्णाली प्रदेश",
        
      },
      "district": {
        "id": 65,
        "did": 607,
        
        "district_en": "Jajarkot",
        "district_np": "जाजरकोट"
      }
    },
    {
      "id": 636,
      "lgid": 60703,
      
      "lgname_en": "Junichaande Rural Mun",
      "lgname_np": "जुनीचाँदे गाउँपालिका",
      "province": {
        "id": 6,
        "province_en": "Karnali Province",
        "province_np": "कर्णाली प्रदेश",
        
      },
      "district": {
        "id": 65,
        "did": 607,
        
        "district_en": "Jajarkot",
        "district_np": "जाजरकोट"
      }
    },
    {
      "id": 637,
      "lgid": 60704,
      
      "lgname_en": "Chhedagad Municipality",
      "lgname_np": "छेडागाड नगरपालिका",
      "province": {
        "id": 6,
        "province_en": "Karnali Province",
        "province_np": "कर्णाली प्रदेश",
        
      },
      "district": {
        "id": 65,
        "did": 607,
        
        "district_en": "Jajarkot",
        "district_np": "जाजरकोट"
      }
    },
    {
      "id": 638,
      "lgid": 60705,
      
      "lgname_en": "Shibalaya Rural Mun",
      "lgname_np": "शिवालय गाउँपालिका",
      "province": {
        "id": 6,
        "province_en": "Karnali Province",
        "province_np": "कर्णाली प्रदेश",
        
      },
      "district": {
        "id": 65,
        "did": 607,
        
        "district_en": "Jajarkot",
        "district_np": "जाजरकोट"
      }
    },
    {
      "id": 639,
      "lgid": 60706,
      
      "lgname_en": "Bheri Municipality",
      "lgname_np": "भेरी नगरपालिका",
      "province": {
        "id": 6,
        "province_en": "Karnali Province",
        "province_np": "कर्णाली प्रदेश",
        
      },
      "district": {
        "id": 65,
        "did": 607,
        
        "district_en": "Jajarkot",
        "district_np": "जाजरकोट"
      }
    },
    {
      "id": 640,
      "lgid": 60707,
      
      "lgname_en": "Nalgad Municipality",
      "lgname_np": "नलगाड नगरपालिका",
      "province": {
        "id": 6,
        "province_en": "Karnali Province",
        "province_np": "कर्णाली प्रदेश",
        
      },
      "district": {
        "id": 65,
        "did": 607,
        
        "district_en": "Jajarkot",
        "district_np": "जाजरकोट"
      }
    },
    {
      "id": 641,
      "lgid": 60801,
      
      "lgname_en": "Aathbiskot Municipality",
      "lgname_np": "आठबिसकोट नगरपालिका",
      "province": {
        "id": 6,
        "province_en": "Karnali Province",
        "province_np": "कर्णाली प्रदेश",
        
      },
      "district": {
        "id": 66,
        "did": 608,
        
        "district_en": "Rukum (West)",
        "district_np": "रुकुम (पश्चिम भाग)"
      }
    },
    {
      "id": 642,
      "lgid": 60802,
      
      "lgname_en": "Sanibheri Rural Mun",
      "lgname_np": "सानी भेरी गाउँपालिका",
      "province": {
        "id": 6,
        "province_en": "Karnali Province",
        "province_np": "कर्णाली प्रदेश",
        
      },
      "district": {
        "id": 66,
        "did": 608,
        
        "district_en": "Rukum (West)",
        "district_np": "रुकुम (पश्चिम भाग)"
      }
    },
    {
      "id": 643,
      "lgid": 60803,
      
      "lgname_en": "Banphikot Rural Mun",
      "lgname_np": "बाँफिकोट गाउँपालिका",
      "province": {
        "id": 6,
        "province_en": "Karnali Province",
        "province_np": "कर्णाली प्रदेश",
        
      },
      "district": {
        "id": 66,
        "did": 608,
        
        "district_en": "Rukum (West)",
        "district_np": "रुकुम (पश्चिम भाग)"
      }
    },
    {
      "id": 644,
      "lgid": 60804,
      
      "lgname_en": "Musikot Municipality",
      "lgname_np": "मुसिकोट नगरपालिका",
      "province": {
        "id": 6,
        "province_en": "Karnali Province",
        "province_np": "कर्णाली प्रदेश",
        
      },
      "district": {
        "id": 66,
        "did": 608,
        
        "district_en": "Rukum (West)",
        "district_np": "रुकुम (पश्चिम भाग)"
      }
    },
    {
      "id": 645,
      "lgid": 60805,
      
      "lgname_en": "Triveni Rural Mun",
      "lgname_np": "त्रिवेणी गाउँपालिका",
      "province": {
        "id": 6,
        "province_en": "Karnali Province",
        "province_np": "कर्णाली प्रदेश",
        
      },
      "district": {
        "id": 66,
        "did": 608,
        
        "district_en": "Rukum (West)",
        "district_np": "रुकुम (पश्चिम भाग)"
      }
    },
    {
      "id": 646,
      "lgid": 60806,
      
      "lgname_en": "Chaurjahari Municipality",
      "lgname_np": "चौरजहारी नगरपालिका",
      "province": {
        "id": 6,
        "province_en": "Karnali Province",
        "province_np": "कर्णाली प्रदेश",
        
      },
      "district": {
        "id": 66,
        "did": 608,
        
        "district_en": "Rukum (West)",
        "district_np": "रुकुम (पश्चिम भाग)"
      }
    },
    {
      "id": 647,
      "lgid": 60901,
      
      "lgname_en": "Darma Rural Mun",
      "lgname_np": "दार्मा गाउँपालिका",
      "province": {
        "id": 6,
        "province_en": "Karnali Province",
        "province_np": "कर्णाली प्रदेश",
        
      },
      "district": {
        "id": 67,
        "did": 609,
        
        "district_en": "Salyan",
        "district_np": "सल्यान"
      }
    },
    {
      "id": 648,
      "lgid": 60902,
      
      "lgname_en": "Kumakh Rural Mun",
      "lgname_np": "कुमाख गाउँपालिका",
      "province": {
        "id": 6,
        "province_en": "Karnali Province",
        "province_np": "कर्णाली प्रदेश",
        
      },
      "district": {
        "id": 67,
        "did": 609,
        
        "district_en": "Salyan",
        "district_np": "सल्यान"
      }
    },
    {
      "id": 649,
      "lgid": 60903,
      
      "lgname_en": "Bangadkupinde Municipality",
      "lgname_np": "बनगाड कुपिण्डे नगरपालिका",
      "province": {
        "id": 6,
        "province_en": "Karnali Province",
        "province_np": "कर्णाली प्रदेश",
        
      },
      "district": {
        "id": 67,
        "did": 609,
        
        "district_en": "Salyan",
        "district_np": "सल्यान"
      }
    },
    {
      "id": 650,
      "lgid": 60904,
      
      "lgname_en": "Siddha Kumakh Rural Mun",
      "lgname_np": "सिद्ध कुमाख गाउँपालिका",
      "province": {
        "id": 6,
        "province_en": "Karnali Province",
        "province_np": "कर्णाली प्रदेश",
        
      },
      "district": {
        "id": 67,
        "did": 609,
        
        "district_en": "Salyan",
        "district_np": "सल्यान"
      }
    },
    {
      "id": 651,
      "lgid": 60905,
      
      "lgname_en": "Bagchaur Municipality",
      "lgname_np": "बागचौर नगरपालिका",
      "province": {
        "id": 6,
        "province_en": "Karnali Province",
        "province_np": "कर्णाली प्रदेश",
        
      },
      "district": {
        "id": 67,
        "did": 609,
        
        "district_en": "Salyan",
        "district_np": "सल्यान"
      }
    },
    {
      "id": 652,
      "lgid": 60906,
      
      "lgname_en": "Chhatreshwori Rural Mun",
      "lgname_np": "छत्रेश्वरी गाउँपालिका",
      "province": {
        "id": 6,
        "province_en": "Karnali Province",
        "province_np": "कर्णाली प्रदेश",
        
      },
      "district": {
        "id": 67,
        "did": 609,
        
        "district_en": "Salyan",
        "district_np": "सल्यान"
      }
    },
    {
      "id": 653,
      "lgid": 60907,
      
      "lgname_en": "Sharada Municipality",
      "lgname_np": "शारदा नगरपालिका",
      "province": {
        "id": 6,
        "province_en": "Karnali Province",
        "province_np": "कर्णाली प्रदेश",
        
      },
      "district": {
        "id": 67,
        "did": 609,
        
        "district_en": "Salyan",
        "district_np": "सल्यान"
      }
    },
    {
      "id": 654,
      "lgid": 60908,
      
      "lgname_en": "Kalimati Rural Mun",
      "lgname_np": "कालिमाटी गाउँपालिका",
      "province": {
        "id": 6,
        "province_en": "Karnali Province",
        "province_np": "कर्णाली प्रदेश",
        
      },
      "district": {
        "id": 67,
        "did": 609,
        
        "district_en": "Salyan",
        "district_np": "सल्यान"
      }
    },
    {
      "id": 655,
      "lgid": 60909,
      
      "lgname_en": "Triveni Rural Mun",
      "lgname_np": "त्रिवेणी गाउँपालिका",
      "province": {
        "id": 6,
        "province_en": "Karnali Province",
        "province_np": "कर्णाली प्रदेश",
        
      },
      "district": {
        "id": 67,
        "did": 609,
        
        "district_en": "Salyan",
        "district_np": "सल्यान"
      }
    },
    {
      "id": 656,
      "lgid": 60910,
      
      "lgname_en": "Kapurkot Rural Mun",
      "lgname_np": "कपुरकोट गाउँपालिका",
      "province": {
        "id": 6,
        "province_en": "Karnali Province",
        "province_np": "कर्णाली प्रदेश",
        
      },
      "district": {
        "id": 67,
        "did": 609,
        
        "district_en": "Salyan",
        "district_np": "सल्यान"
      }
    },
    {
      "id": 657,
      "lgid": 61001,
      
      "lgname_en": "Simta Rural Mun",
      "lgname_np": "सिम्ता गाउँपालिका",
      "province": {
        "id": 6,
        "province_en": "Karnali Province",
        "province_np": "कर्णाली प्रदेश",
        
      },
      "district": {
        "id": 68,
        "did": 610,
        
        "district_en": "Surkhet",
        "district_np": "सुर्खेत"
      }
    },
    {
      "id": 658,
      "lgid": 61002,
      
      "lgname_en": "Chingad Rural Mun",
      "lgname_np": "चिङ्गाड गाउँपालिका",
      "province": {
        "id": 6,
        "province_en": "Karnali Province",
        "province_np": "कर्णाली प्रदेश",
        
      },
      "district": {
        "id": 68,
        "did": 610,
        
        "district_en": "Surkhet",
        "district_np": "सुर्खेत"
      }
    },
    {
      "id": 659,
      "lgid": 61003,
      
      "lgname_en": "Lekbeshi Municipality",
      "lgname_np": "लेकवेशी नगरपालिका",
      "province": {
        "id": 6,
        "province_en": "Karnali Province",
        "province_np": "कर्णाली प्रदेश",
        
      },
      "district": {
        "id": 68,
        "did": 610,
        
        "district_en": "Surkhet",
        "district_np": "सुर्खेत"
      }
    },
    {
      "id": 660,
      "lgid": 61004,
      
      "lgname_en": "Gurbhakot Municipality",
      "lgname_np": "गुर्भाकोट नगरपालिका",
      "province": {
        "id": 6,
        "province_en": "Karnali Province",
        "province_np": "कर्णाली प्रदेश",
        
      },
      "district": {
        "id": 68,
        "did": 610,
        
        "district_en": "Surkhet",
        "district_np": "सुर्खेत"
      }
    },
    {
      "id": 661,
      "lgid": 61005,
      
      "lgname_en": "Bheriganga Municipality",
      "lgname_np": "भेरीगंगा नगरपालिका",
      "province": {
        "id": 6,
        "province_en": "Karnali Province",
        "province_np": "कर्णाली प्रदेश",
        
      },
      "district": {
        "id": 68,
        "did": 610,
        
        "district_en": "Surkhet",
        "district_np": "सुर्खेत"
      }
    },
    {
      "id": 662,
      "lgid": 61006,
      
      "lgname_en": "Birendranagar Municipality",
      "lgname_np": "बीरेन्द्रनगर नगरपालिका",
      "province": {
        "id": 6,
        "province_en": "Karnali Province",
        "province_np": "कर्णाली प्रदेश",
        
      },
      "district": {
        "id": 68,
        "did": 610,
        
        "district_en": "Surkhet",
        "district_np": "सुर्खेत"
      }
    },
    {
      "id": 663,
      "lgid": 61007,
      
      "lgname_en": "Barahatal Rural Mun",
      "lgname_np": "बराहताल गाउँपालिका",
      "province": {
        "id": 6,
        "province_en": "Karnali Province",
        "province_np": "कर्णाली प्रदेश",
        
      },
      "district": {
        "id": 68,
        "did": 610,
        
        "district_en": "Surkhet",
        "district_np": "सुर्खेत"
      }
    },
    {
      "id": 664,
      "lgid": 61008,
      
      "lgname_en": "Panchapuri Municipality",
      "lgname_np": "पञ्चपुरी नगरपालिका",
      "province": {
        "id": 6,
        "province_en": "Karnali Province",
        "province_np": "कर्णाली प्रदेश",
        
      },
      "district": {
        "id": 68,
        "did": 610,
        
        "district_en": "Surkhet",
        "district_np": "सुर्खेत"
      }
    },
    {
      "id": 665,
      "lgid": 61009,
      
      "lgname_en": "Chaukune Rural Mun",
      "lgname_np": "चौकुने गाउँपालिका",
      "province": {
        "id": 6,
        "province_en": "Karnali Province",
        "province_np": "कर्णाली प्रदेश",
        
      },
      "district": {
        "id": 68,
        "did": 610,
        
        "district_en": "Surkhet",
        "district_np": "सुर्खेत"
      }
    },
    {
      "id": 666,
      "lgid": 70101,
      
      "lgname_en": "Himali Rural Mun",
      "lgname_np": "हिमाली गाउँपालिका",
      "province": {
        "id": 7,
        "province_en": "Sudur Paschim Province",
        "province_np": "सुदुर पश्चिम प्रदेश",
        
      },
      "district": {
        "id": 69,
        "did": 701,
        
        "district_en": "Bajura",
        "district_np": "बाजुरा"
      }
    },
    {
      "id": 667,
      "lgid": 70102,
      
      "lgname_en": "Gaumul Rural Mun",
      "lgname_np": "गौमुल गाउँपालिका",
      "province": {
        "id": 7,
        "province_en": "Sudur Paschim Province",
        "province_np": "सुदुर पश्चिम प्रदेश",
        
      },
      "district": {
        "id": 69,
        "did": 701,
        
        "district_en": "Bajura",
        "district_np": "बाजुरा"
      }
    },
    {
      "id": 668,
      "lgid": 70103,
      
      "lgname_en": "Budhinanda Municipality",
      "lgname_np": "बुढीनन्दा नगरपालिका",
      "province": {
        "id": 7,
        "province_en": "Sudur Paschim Province",
        "province_np": "सुदुर पश्चिम प्रदेश",
        
      },
      "district": {
        "id": 69,
        "did": 701,
        
        "district_en": "Bajura",
        "district_np": "बाजुरा"
      }
    },
    {
      "id": 669,
      "lgid": 70104,
      
      "lgname_en": "Swamikartik Khapar Rural Mun",
      "lgname_np": "स्वामीकार्तिक खापर गाउँपालिका",
      "province": {
        "id": 7,
        "province_en": "Sudur Paschim Province",
        "province_np": "सुदुर पश्चिम प्रदेश",
        
      },
      "district": {
        "id": 69,
        "did": 701,
        
        "district_en": "Bajura",
        "district_np": "बाजुरा"
      }
    },
    {
      "id": 670,
      "lgid": 70105,
      
      "lgname_en": "Jagannath Rural Mun",
      "lgname_np": "जगन्‍नाथ गाउँपालिका",
      "province": {
        "id": 7,
        "province_en": "Sudur Paschim Province",
        "province_np": "सुदुर पश्चिम प्रदेश",
        
      },
      "district": {
        "id": 69,
        "did": 701,
        
        "district_en": "Bajura",
        "district_np": "बाजुरा"
      }
    },
    {
      "id": 671,
      "lgid": 70106,
      
      "lgname_en": "Badimalika Municipality",
      "lgname_np": "बडीमालिका नगरपालिका",
      "province": {
        "id": 7,
        "province_en": "Sudur Paschim Province",
        "province_np": "सुदुर पश्चिम प्रदेश",
        
      },
      "district": {
        "id": 69,
        "did": 701,
        
        "district_en": "Bajura",
        "district_np": "बाजुरा"
      }
    },
    {
      "id": 672,
      "lgid": 70107,
      
      "lgname_en": "Khaptad Chhededaha Rural Mun",
      "lgname_np": "खप्तड छेडेदह गाउँपालिका",
      "province": {
        "id": 7,
        "province_en": "Sudur Paschim Province",
        "province_np": "सुदुर पश्चिम प्रदेश",
        
      },
      "district": {
        "id": 69,
        "did": 701,
        
        "district_en": "Bajura",
        "district_np": "बाजुरा"
      }
    },
    {
      "id": 673,
      "lgid": 70108,
      
      "lgname_en": "Budhiganga Municipality",
      "lgname_np": "बुढीगंगा नगरपालिका",
      "province": {
        "id": 7,
        "province_en": "Sudur Paschim Province",
        "province_np": "सुदुर पश्चिम प्रदेश",
        
      },
      "district": {
        "id": 69,
        "did": 701,
        
        "district_en": "Bajura",
        "district_np": "बाजुरा"
      }
    },
    {
      "id": 674,
      "lgid": 70109,
      
      "lgname_en": "Triveni Municipality",
      "lgname_np": "त्रिवेणी नगरपालिका",
      "province": {
        "id": 7,
        "province_en": "Sudur Paschim Province",
        "province_np": "सुदुर पश्चिम प्रदेश",
        
      },
      "district": {
        "id": 69,
        "did": 701,
        
        "district_en": "Bajura",
        "district_np": "बाजुरा"
      }
    },
    {
      "id": 675,
      "lgid": 70201,
      
      "lgname_en": "Saipal Rural Mun",
      "lgname_np": "साइपाल गाउँपालिका ",
      "province": {
        "id": 7,
        "province_en": "Sudur Paschim Province",
        "province_np": "सुदुर पश्चिम प्रदेश",
        
      },
      "district": {
        "id": 70,
        "did": 702,
        
        "district_en": "Bajhang",
        "district_np": "बझाङ"
      }
    },
    {
      "id": 676,
      "lgid": 70202,
      
      "lgname_en": "Bungal Municipality",
      "lgname_np": "बुंगल नगरपालिका",
      "province": {
        "id": 7,
        "province_en": "Sudur Paschim Province",
        "province_np": "सुदुर पश्चिम प्रदेश",
        
      },
      "district": {
        "id": 70,
        "did": 702,
        
        "district_en": "Bajhang",
        "district_np": "बझाङ"
      }
    },
    {
      "id": 677,
      "lgid": 70203,
      
      "lgname_en": "Surma Rural Mun",
      "lgname_np": "सूर्मा गाउँपालिका ",
      "province": {
        "id": 7,
        "province_en": "Sudur Paschim Province",
        "province_np": "सुदुर पश्चिम प्रदेश",
        
      },
      "district": {
        "id": 70,
        "did": 702,
        
        "district_en": "Bajhang",
        "district_np": "बझाङ"
      }
    },
    {
      "id": 678,
      "lgid": 70204,
      
      "lgname_en": "Talkot Rural Mun",
      "lgname_np": "तलकोट गाउँपालिका",
      "province": {
        "id": 7,
        "province_en": "Sudur Paschim Province",
        "province_np": "सुदुर पश्चिम प्रदेश",
        
      },
      "district": {
        "id": 70,
        "did": 702,
        
        "district_en": "Bajhang",
        "district_np": "बझाङ"
      }
    },
    {
      "id": 679,
      "lgid": 70205,
      
      "lgname_en": "Masta Rural Mun",
      "lgname_np": "मष्टा गाउँपालिका",
      "province": {
        "id": 7,
        "province_en": "Sudur Paschim Province",
        "province_np": "सुदुर पश्चिम प्रदेश",
        
      },
      "district": {
        "id": 70,
        "did": 702,
        
        "district_en": "Bajhang",
        "district_np": "बझाङ"
      }
    },
    {
      "id": 680,
      "lgid": 70206,
      
      "lgname_en": "Jayaprithvi Municipality",
      "lgname_np": "जयपृथ्वी नगरपालिका",
      "province": {
        "id": 7,
        "province_en": "Sudur Paschim Province",
        "province_np": "सुदुर पश्चिम प्रदेश",
        
      },
      "district": {
        "id": 70,
        "did": 702,
        
        "district_en": "Bajhang",
        "district_np": "बझाङ"
      }
    },
    {
      "id": 681,
      "lgid": 70207,
      
      "lgname_en": "Chhabispathivera Rural Mun",
      "lgname_np": "छबिसपाथिभेरा गाउँपालिका",
      "province": {
        "id": 7,
        "province_en": "Sudur Paschim Province",
        "province_np": "सुदुर पश्चिम प्रदेश",
        
      },
      "district": {
        "id": 70,
        "did": 702,
        
        "district_en": "Bajhang",
        "district_np": "बझाङ"
      }
    },
    {
      "id": 682,
      "lgid": 70208,
      
      "lgname_en": "Durgathali Rural Mun",
      "lgname_np": "दुर्गाथली गाउँपालिका",
      "province": {
        "id": 7,
        "province_en": "Sudur Paschim Province",
        "province_np": "सुदुर पश्चिम प्रदेश",
        
      },
      "district": {
        "id": 70,
        "did": 702,
        
        "district_en": "Bajhang",
        "district_np": "बझाङ"
      }
    },
    {
      "id": 683,
      "lgid": 70209,
      
      "lgname_en": "Kedarasyu Rural Mun",
      "lgname_np": "केदारस्युँ गाउँपालिका",
      "province": {
        "id": 7,
        "province_en": "Sudur Paschim Province",
        "province_np": "सुदुर पश्चिम प्रदेश",
        
      },
      "district": {
        "id": 70,
        "did": 702,
        
        "district_en": "Bajhang",
        "district_np": "बझाङ"
      }
    },
    {
      "id": 684,
      "lgid": 70210,
      
      "lgname_en": "Bitthadchir Rural Mun",
      "lgname_np": "वित्थडचिर गाउँपालिका",
      "province": {
        "id": 7,
        "province_en": "Sudur Paschim Province",
        "province_np": "सुदुर पश्चिम प्रदेश",
        
      },
      "district": {
        "id": 70,
        "did": 702,
        
        "district_en": "Bajhang",
        "district_np": "बझाङ"
      }
    },
    {
      "id": 685,
      "lgid": 70211,
      
      "lgname_en": "Thalara Rural Mun",
      "lgname_np": "थलारा गाउँपालिका",
      "province": {
        "id": 7,
        "province_en": "Sudur Paschim Province",
        "province_np": "सुदुर पश्चिम प्रदेश",
        
      },
      "district": {
        "id": 70,
        "did": 702,
        
        "district_en": "Bajhang",
        "district_np": "बझाङ"
      }
    },
    {
      "id": 686,
      "lgid": 70212,
      
      "lgname_en": "Khaptadchhanna Rural Mun",
      "lgname_np": "खप्तडछान्ना गाउँपालिका",
      "province": {
        "id": 7,
        "province_en": "Sudur Paschim Province",
        "province_np": "सुदुर पश्चिम प्रदेश",
        
      },
      "district": {
        "id": 70,
        "did": 702,
        
        "district_en": "Bajhang",
        "district_np": "बझाङ"
      }
    },
    {
      "id": 687,
      "lgid": 70301,
      
      "lgname_en": "Vyans Rural Mun",
      "lgname_np": "ब्याँस गाउँपालिका",
      "province": {
        "id": 7,
        "province_en": "Sudur Paschim Province",
        "province_np": "सुदुर पश्चिम प्रदेश",
        
      },
      "district": {
        "id": 71,
        "did": 703,
        
        "district_en": "Darchula",
        "district_np": "दार्चुला"
      }
    },
    {
      "id": 688,
      "lgid": 70302,
      
      "lgname_en": "Duhun Rural Mun",
      "lgname_np": "दुहुँ गाउँपालिका",
      "province": {
        "id": 7,
        "province_en": "Sudur Paschim Province",
        "province_np": "सुदुर पश्चिम प्रदेश",
        
      },
      "district": {
        "id": 71,
        "did": 703,
        
        "district_en": "Darchula",
        "district_np": "दार्चुला"
      }
    },
    {
      "id": 689,
      "lgid": 70303,
      
      "lgname_en": "Mahakali Municipality",
      "lgname_np": "महाकाली नगरपालिका",
      "province": {
        "id": 7,
        "province_en": "Sudur Paschim Province",
        "province_np": "सुदुर पश्चिम प्रदेश",
        
      },
      "district": {
        "id": 71,
        "did": 703,
        
        "district_en": "Darchula",
        "district_np": "दार्चुला"
      }
    },
    {
      "id": 690,
      "lgid": 70304,
      
      "lgname_en": "Naugad Rural Mun",
      "lgname_np": "नौगाड गाउँपालिका",
      "province": {
        "id": 7,
        "province_en": "Sudur Paschim Province",
        "province_np": "सुदुर पश्चिम प्रदेश",
        
      },
      "district": {
        "id": 71,
        "did": 703,
        
        "district_en": "Darchula",
        "district_np": "दार्चुला"
      }
    },
    {
      "id": 691,
      "lgid": 70305,
      
      "lgname_en": "Apihimal Rural Mun",
      "lgname_np": "अपिहिमाल गाउँपालिका",
      "province": {
        "id": 7,
        "province_en": "Sudur Paschim Province",
        "province_np": "सुदुर पश्चिम प्रदेश",
        
      },
      "district": {
        "id": 71,
        "did": 703,
        
        "district_en": "Darchula",
        "district_np": "दार्चुला"
      }
    },
    {
      "id": 692,
      "lgid": 70306,
      
      "lgname_en": "Marma Rural Mun",
      "lgname_np": "मार्मा गाउँपालिका",
      "province": {
        "id": 7,
        "province_en": "Sudur Paschim Province",
        "province_np": "सुदुर पश्चिम प्रदेश",
        
      },
      "district": {
        "id": 71,
        "did": 703,
        
        "district_en": "Darchula",
        "district_np": "दार्चुला"
      }
    },
    {
      "id": 693,
      "lgid": 70307,
      
      "lgname_en": "Shailyashikhar Municipality",
      "lgname_np": "शैल्यशिखर नगरपालिका",
      "province": {
        "id": 7,
        "province_en": "Sudur Paschim Province",
        "province_np": "सुदुर पश्चिम प्रदेश",
        
      },
      "district": {
        "id": 71,
        "did": 703,
        
        "district_en": "Darchula",
        "district_np": "दार्चुला"
      }
    },
    {
      "id": 694,
      "lgid": 70308,
      
      "lgname_en": "Malikarjun Rural Mun",
      "lgname_np": "मालिकार्जुन गाउँपालिका",
      "province": {
        "id": 7,
        "province_en": "Sudur Paschim Province",
        "province_np": "सुदुर पश्चिम प्रदेश",
        
      },
      "district": {
        "id": 71,
        "did": 703,
        
        "district_en": "Darchula",
        "district_np": "दार्चुला"
      }
    },
    {
      "id": 695,
      "lgid": 70309,
      
      "lgname_en": "Lekam Rural Mun",
      "lgname_np": "लेकम गाउँपालिका",
      "province": {
        "id": 7,
        "province_en": "Sudur Paschim Province",
        "province_np": "सुदुर पश्चिम प्रदेश",
        
      },
      "district": {
        "id": 71,
        "did": 703,
        
        "district_en": "Darchula",
        "district_np": "दार्चुला"
      }
    },
    {
      "id": 696,
      "lgid": 70401,
      
      "lgname_en": "Dilasaini Rural Mun",
      "lgname_np": "डीलासैनी गाउँपालिका",
      "province": {
        "id": 7,
        "province_en": "Sudur Paschim Province",
        "province_np": "सुदुर पश्चिम प्रदेश",
        
      },
      "district": {
        "id": 72,
        "did": 704,
        
        "district_en": "Baitadi",
        "district_np": "बैतडी"
      }
    },
    {
      "id": 697,
      "lgid": 70402,
      
      "lgname_en": "Dogdakedar Rural Mun",
      "lgname_np": "दोगडाकेदार गाउँपालिका",
      "province": {
        "id": 7,
        "province_en": "Sudur Paschim Province",
        "province_np": "सुदुर पश्चिम प्रदेश",
        
      },
      "district": {
        "id": 72,
        "did": 704,
        
        "district_en": "Baitadi",
        "district_np": "बैतडी"
      }
    },
    {
      "id": 698,
      "lgid": 70403,
      
      "lgname_en": "Purchaudi Municipality",
      "lgname_np": "पुर्चौडी नगरपालिका",
      "province": {
        "id": 7,
        "province_en": "Sudur Paschim Province",
        "province_np": "सुदुर पश्चिम प्रदेश",
        
      },
      "district": {
        "id": 72,
        "did": 704,
        
        "district_en": "Baitadi",
        "district_np": "बैतडी"
      }
    },
    {
      "id": 699,
      "lgid": 70404,
      
      "lgname_en": "Sunarya Rural Mun",
      "lgname_np": "सुर्नया गाउँपालिका",
      "province": {
        "id": 7,
        "province_en": "Sudur Paschim Province",
        "province_np": "सुदुर पश्चिम प्रदेश",
        
      },
      "district": {
        "id": 72,
        "did": 704,
        
        "district_en": "Baitadi",
        "district_np": "बैतडी"
      }
    },
    {
      "id": 700,
      "lgid": 70405,
      
      "lgname_en": "Dasharathchand Municipality",
      "lgname_np": "दशरथचन्द नगरपालिका",
      "province": {
        "id": 7,
        "province_en": "Sudur Paschim Province",
        "province_np": "सुदुर पश्चिम प्रदेश",
        
      },
      "district": {
        "id": 72,
        "did": 704,
        
        "district_en": "Baitadi",
        "district_np": "बैतडी"
      }
    },
    {
      "id": 701,
      "lgid": 70406,
      
      "lgname_en": "Pancheshwor Rural Mun",
      "lgname_np": "पञ्चेश्वर गाउँपालिका",
      "province": {
        "id": 7,
        "province_en": "Sudur Paschim Province",
        "province_np": "सुदुर पश्चिम प्रदेश",
        
      },
      "district": {
        "id": 72,
        "did": 704,
        
        "district_en": "Baitadi",
        "district_np": "बैतडी"
      }
    },
    {
      "id": 702,
      "lgid": 70407,
      
      "lgname_en": "Shivanath Rural Mun",
      "lgname_np": "शिवनाथ गाउँपालिका",
      "province": {
        "id": 7,
        "province_en": "Sudur Paschim Province",
        "province_np": "सुदुर पश्चिम प्रदेश",
        
      },
      "district": {
        "id": 72,
        "did": 704,
        
        "district_en": "Baitadi",
        "district_np": "बैतडी"
      }
    },
    {
      "id": 703,
      "lgid": 70408,
      
      "lgname_en": "Melauli Municipality",
      "lgname_np": "मेलौली नगरपालिका",
      "province": {
        "id": 7,
        "province_en": "Sudur Paschim Province",
        "province_np": "सुदुर पश्चिम प्रदेश",
        
      },
      "district": {
        "id": 72,
        "did": 704,
        
        "district_en": "Baitadi",
        "district_np": "बैतडी"
      }
    },
    {
      "id": 704,
      "lgid": 70409,
      
      "lgname_en": "Patan Municipality",
      "lgname_np": "पाटन नगरपालिका",
      "province": {
        "id": 7,
        "province_en": "Sudur Paschim Province",
        "province_np": "सुदुर पश्चिम प्रदेश",
        
      },
      "district": {
        "id": 72,
        "did": 704,
        
        "district_en": "Baitadi",
        "district_np": "बैतडी"
      }
    },
    {
      "id": 705,
      "lgid": 70410,
      
      "lgname_en": "Sigas Rural Mun",
      "lgname_np": "सिगास गाउँपालिका",
      "province": {
        "id": 7,
        "province_en": "Sudur Paschim Province",
        "province_np": "सुदुर पश्चिम प्रदेश",
        
      },
      "district": {
        "id": 72,
        "did": 704,
        
        "district_en": "Baitadi",
        "district_np": "बैतडी"
      }
    },
    {
      "id": 706,
      "lgid": 70501,
      
      "lgname_en": "Navadurga Rural Mun",
      "lgname_np": "नवदुर्गा गाउँपालिका",
      "province": {
        "id": 7,
        "province_en": "Sudur Paschim Province",
        "province_np": "सुदुर पश्चिम प्रदेश",
        
      },
      "district": {
        "id": 73,
        "did": 705,
        
        "district_en": "Dadeldhura",
        "district_np": "डडेलधुरा"
      }
    },
    {
      "id": 707,
      "lgid": 70502,
      
      "lgname_en": "Amargadhi Municipality",
      "lgname_np": "अमरगढी नगरपालिका",
      "province": {
        "id": 7,
        "province_en": "Sudur Paschim Province",
        "province_np": "सुदुर पश्चिम प्रदेश",
        
      },
      "district": {
        "id": 73,
        "did": 705,
        
        "district_en": "Dadeldhura",
        "district_np": "डडेलधुरा"
      }
    },
    {
      "id": 708,
      "lgid": 70503,
      
      "lgname_en": "Ajayameru Rural Mun",
      "lgname_np": "अजयमेरु गाउँपालिका",
      "province": {
        "id": 7,
        "province_en": "Sudur Paschim Province",
        "province_np": "सुदुर पश्चिम प्रदेश",
        
      },
      "district": {
        "id": 73,
        "did": 705,
        
        "district_en": "Dadeldhura",
        "district_np": "डडेलधुरा"
      }
    },
    {
      "id": 709,
      "lgid": 70504,
      
      "lgname_en": "Bhageshwor Rural Mun",
      "lgname_np": "भागेश्वर गाउँपालिका",
      "province": {
        "id": 7,
        "province_en": "Sudur Paschim Province",
        "province_np": "सुदुर पश्चिम प्रदेश",
        
      },
      "district": {
        "id": 73,
        "did": 705,
        
        "district_en": "Dadeldhura",
        "district_np": "डडेलधुरा"
      }
    },
    {
      "id": 710,
      "lgid": 70505,
      
      "lgname_en": "Parshuram Municipality",
      "lgname_np": "परशुराम नगरपालिका",
      "province": {
        "id": 7,
        "province_en": "Sudur Paschim Province",
        "province_np": "सुदुर पश्चिम प्रदेश",
        
      },
      "district": {
        "id": 73,
        "did": 705,
        
        "district_en": "Dadeldhura",
        "district_np": "डडेलधुरा"
      }
    },
    {
      "id": 711,
      "lgid": 70506,
      
      "lgname_en": "Aalital Rural Mun",
      "lgname_np": "आलिताल गाउँपालिका",
      "province": {
        "id": 7,
        "province_en": "Sudur Paschim Province",
        "province_np": "सुदुर पश्चिम प्रदेश",
        
      },
      "district": {
        "id": 73,
        "did": 705,
        
        "district_en": "Dadeldhura",
        "district_np": "डडेलधुरा"
      }
    },
    {
      "id": 712,
      "lgid": 70507,
      
      "lgname_en": "Ganyapadhura Rural Mun",
      "lgname_np": "गन्यापधुरा गाउँपालिका",
      "province": {
        "id": 7,
        "province_en": "Sudur Paschim Province",
        "province_np": "सुदुर पश्चिम प्रदेश",
        
      },
      "district": {
        "id": 73,
        "did": 705,
        
        "district_en": "Dadeldhura",
        "district_np": "डडेलधुरा"
      }
    },
    {
      "id": 713,
      "lgid": 70601,
      
      "lgname_en": "Purbichauki Rural Mun",
      "lgname_np": "पूर्वीचौकी गाउँपालिका",
      "province": {
        "id": 7,
        "province_en": "Sudur Paschim Province",
        "province_np": "सुदुर पश्चिम प्रदेश",
        
      },
      "district": {
        "id": 74,
        "did": 706,
        
        "district_en": "Doti",
        "district_np": "डोटी"
      }
    },
    {
      "id": 714,
      "lgid": 70602,
      
      "lgname_en": "Sayal Rural Mun",
      "lgname_np": "सायल गाउँपालिका",
      "province": {
        "id": 7,
        "province_en": "Sudur Paschim Province",
        "province_np": "सुदुर पश्चिम प्रदेश",
        
      },
      "district": {
        "id": 74,
        "did": 706,
        
        "district_en": "Doti",
        "district_np": "डोटी"
      }
    },
    {
      "id": 715,
      "lgid": 70603,
      
      "lgname_en": "Aadarsha Rural Mun",
      "lgname_np": "आदर्श गाउँपालिका",
      "province": {
        "id": 7,
        "province_en": "Sudur Paschim Province",
        "province_np": "सुदुर पश्चिम प्रदेश",
        
      },
      "district": {
        "id": 74,
        "did": 706,
        
        "district_en": "Doti",
        "district_np": "डोटी"
      }
    },
    {
      "id": 716,
      "lgid": 70604,
      
      "lgname_en": "Shikhar Municipality",
      "lgname_np": "शिखर नगरपालिका",
      "province": {
        "id": 7,
        "province_en": "Sudur Paschim Province",
        "province_np": "सुदुर पश्चिम प्रदेश",
        
      },
      "district": {
        "id": 74,
        "did": 706,
        
        "district_en": "Doti",
        "district_np": "डोटी"
      }
    },
    {
      "id": 717,
      "lgid": 70605,
      
      "lgname_en": "Dipayalsilgadhi Municipality",
      "lgname_np": "दिपायल सिलगढी नगरपालिका",
      "province": {
        "id": 7,
        "province_en": "Sudur Paschim Province",
        "province_np": "सुदुर पश्चिम प्रदेश",
        
      },
      "district": {
        "id": 74,
        "did": 706,
        
        "district_en": "Doti",
        "district_np": "डोटी"
      }
    },
    {
      "id": 718,
      "lgid": 70606,
      
      "lgname_en": "Kisingh Rural Mun",
      "lgname_np": "के.आई.सिं. गाउँपालिका",
      "province": {
        "id": 7,
        "province_en": "Sudur Paschim Province",
        "province_np": "सुदुर पश्चिम प्रदेश",
        
      },
      "district": {
        "id": 74,
        "did": 706,
        
        "district_en": "Doti",
        "district_np": "डोटी"
      }
    },
    {
      "id": 719,
      "lgid": 70607,
      
      "lgname_en": "Bogatan Phudsil Rural Mun",
      "lgname_np": "बोगटान फुड्सिल गाउँपालिका",
      "province": {
        "id": 7,
        "province_en": "Sudur Paschim Province",
        "province_np": "सुदुर पश्चिम प्रदेश",
        
      },
      "district": {
        "id": 74,
        "did": 706,
        
        "district_en": "Doti",
        "district_np": "डोटी"
      }
    },
    {
      "id": 720,
      "lgid": 70608,
      
      "lgname_en": "Badikedar Rural Mun",
      "lgname_np": "बडीकेदार गाउँपालिका",
      "province": {
        "id": 7,
        "province_en": "Sudur Paschim Province",
        "province_np": "सुदुर पश्चिम प्रदेश",
        
      },
      "district": {
        "id": 74,
        "did": 706,
        
        "district_en": "Doti",
        "district_np": "डोटी"
      }
    },
    {
      "id": 721,
      "lgid": 70609,
      
      "lgname_en": "Jorayal Rural Mun",
      "lgname_np": "जोरायल गाउँपालिका",
      "province": {
        "id": 7,
        "province_en": "Sudur Paschim Province",
        "province_np": "सुदुर पश्चिम प्रदेश",
        
      },
      "district": {
        "id": 74,
        "did": 706,
        
        "district_en": "Doti",
        "district_np": "डोटी"
      }
    },
    {
      "id": 722,
      "lgid": 70701,
      
      "lgname_en": "Panchadewalbinayak Municipality",
      "lgname_np": "पन्चदेवल विनायक नगरपालिका",
      "province": {
        "id": 7,
        "province_en": "Sudur Paschim Province",
        "province_np": "सुदुर पश्चिम प्रदेश",
        
      },
      "district": {
        "id": 75,
        "did": 707,
        
        "district_en": "Achham",
        "district_np": "अछाम"
      }
    },
    {
      "id": 723,
      "lgid": 70702,
      
      "lgname_en": "Ramaroshan Rural Mun",
      "lgname_np": "रामारोशन गाउँपालिका",
      "province": {
        "id": 7,
        "province_en": "Sudur Paschim Province",
        "province_np": "सुदुर पश्चिम प्रदेश",
        
      },
      "district": {
        "id": 75,
        "did": 707,
        
        "district_en": "Achham",
        "district_np": "अछाम"
      }
    },
    {
      "id": 724,
      "lgid": 70703,
      
      "lgname_en": "Mellekh Rural Mun",
      "lgname_np": "मेल्लेख गाउँपालिका",
      "province": {
        "id": 7,
        "province_en": "Sudur Paschim Province",
        "province_np": "सुदुर पश्चिम प्रदेश",
        
      },
      "district": {
        "id": 75,
        "did": 707,
        
        "district_en": "Achham",
        "district_np": "अछाम"
      }
    },
    {
      "id": 725,
      "lgid": 70704,
      
      "lgname_en": "Sanfebagar Municipality",
      "lgname_np": "साँफेबगर नगरपालिका",
      "province": {
        "id": 7,
        "province_en": "Sudur Paschim Province",
        "province_np": "सुदुर पश्चिम प्रदेश",
        
      },
      "district": {
        "id": 75,
        "did": 707,
        
        "district_en": "Achham",
        "district_np": "अछाम"
      }
    },
    {
      "id": 726,
      "lgid": 70705,
      
      "lgname_en": "Chaurpati Rural Mun",
      "lgname_np": "चौरपाटी गाउँपालिका",
      "province": {
        "id": 7,
        "province_en": "Sudur Paschim Province",
        "province_np": "सुदुर पश्चिम प्रदेश",
        
      },
      "district": {
        "id": 75,
        "did": 707,
        
        "district_en": "Achham",
        "district_np": "अछाम"
      }
    },
    {
      "id": 727,
      "lgid": 70706,
      
      "lgname_en": "Mangalsen Municipality",
      "lgname_np": "मंगलसेन नगरपालिका",
      "province": {
        "id": 7,
        "province_en": "Sudur Paschim Province",
        "province_np": "सुदुर पश्चिम प्रदेश",
        
      },
      "district": {
        "id": 75,
        "did": 707,
        
        "district_en": "Achham",
        "district_np": "अछाम"
      }
    },
    {
      "id": 728,
      "lgid": 70707,
      
      "lgname_en": "Bannigadhijaygadh Rural Mun",
      "lgname_np": "बान्निगढी जयगढ गाउँपालिका",
      "province": {
        "id": 7,
        "province_en": "Sudur Paschim Province",
        "province_np": "सुदुर पश्चिम प्रदेश",
        
      },
      "district": {
        "id": 75,
        "did": 707,
        
        "district_en": "Achham",
        "district_np": "अछाम"
      }
    },
    {
      "id": 729,
      "lgid": 70708,
      
      "lgname_en": "Kamalbazar Municipality",
      "lgname_np": "कमलबजार नगरपालिका",
      "province": {
        "id": 7,
        "province_en": "Sudur Paschim Province",
        "province_np": "सुदुर पश्चिम प्रदेश",
        
      },
      "district": {
        "id": 75,
        "did": 707,
        
        "district_en": "Achham",
        "district_np": "अछाम"
      }
    },
    {
      "id": 730,
      "lgid": 70709,
      
      "lgname_en": "Dhakari Rural Mun",
      "lgname_np": "ढकारी गाउँपालिका",
      "province": {
        "id": 7,
        "province_en": "Sudur Paschim Province",
        "province_np": "सुदुर पश्चिम प्रदेश",
        
      },
      "district": {
        "id": 75,
        "did": 707,
        
        "district_en": "Achham",
        "district_np": "अछाम"
      }
    },
    {
      "id": 731,
      "lgid": 70710,
      
      "lgname_en": "Turmakhad Rural Mun",
      "lgname_np": "तुर्माखाँद गाउँपालिका",
      "province": {
        "id": 7,
        "province_en": "Sudur Paschim Province",
        "province_np": "सुदुर पश्चिम प्रदेश",
        
      },
      "district": {
        "id": 75,
        "did": 707,
        
        "district_en": "Achham",
        "district_np": "अछाम"
      }
    },
    {
      "id": 732,
      "lgid": 70801,
      
      "lgname_en": "Mohanyal Rural Mun",
      "lgname_np": "मोहन्याल गाउँपालिका",
      "province": {
        "id": 7,
        "province_en": "Sudur Paschim Province",
        "province_np": "सुदुर पश्चिम प्रदेश",
        
      },
      "district": {
        "id": 76,
        "did": 708,
        
        "district_en": "Kailali",
        "district_np": "कैलाली"
      }
    },
    {
      "id": 733,
      "lgid": 70802,
      
      "lgname_en": "Chure Rural Mun",
      "lgname_np": "चुरे गाउँपालिका",
      "province": {
        "id": 7,
        "province_en": "Sudur Paschim Province",
        "province_np": "सुदुर पश्चिम प्रदेश",
        
      },
      "district": {
        "id": 76,
        "did": 708,
        
        "district_en": "Kailali",
        "district_np": "कैलाली"
      }
    },
    {
      "id": 734,
      "lgid": 70803,
      
      "lgname_en": "Godawari Municipality",
      "lgname_np": "गोदावरी नगरपालिका",
      "province": {
        "id": 7,
        "province_en": "Sudur Paschim Province",
        "province_np": "सुदुर पश्चिम प्रदेश",
        
      },
      "district": {
        "id": 76,
        "did": 708,
        
        "district_en": "Kailali",
        "district_np": "कैलाली"
      }
    },
    {
      "id": 735,
      "lgid": 70804,
      
      "lgname_en": "Gauriganga Municipality",
      "lgname_np": "गौरीगंगा नगरपालिका",
      "province": {
        "id": 7,
        "province_en": "Sudur Paschim Province",
        "province_np": "सुदुर पश्चिम प्रदेश",
        
      },
      "district": {
        "id": 76,
        "did": 708,
        
        "district_en": "Kailali",
        "district_np": "कैलाली"
      }
    },
    {
      "id": 736,
      "lgid": 70805,
      
      "lgname_en": "Ghodaghodi Municipality",
      "lgname_np": "घोडाघोडी नगरपालिका",
      "province": {
        "id": 7,
        "province_en": "Sudur Paschim Province",
        "province_np": "सुदुर पश्चिम प्रदेश",
        
      },
      "district": {
        "id": 76,
        "did": 708,
        
        "district_en": "Kailali",
        "district_np": "कैलाली"
      }
    },
    {
      "id": 737,
      "lgid": 70806,
      
      "lgname_en": "Bardgoriya Rural Mun",
      "lgname_np": "बर्दगोरिया गाउँपालिका",
      "province": {
        "id": 7,
        "province_en": "Sudur Paschim Province",
        "province_np": "सुदुर पश्चिम प्रदेश",
        
      },
      "district": {
        "id": 76,
        "did": 708,
        
        "district_en": "Kailali",
        "district_np": "कैलाली"
      }
    },
    {
      "id": 738,
      "lgid": 70807,
      
      "lgname_en": "Lamkichuha Municipality",
      "lgname_np": "लम्कीचुहा नगरपालिका",
      "province": {
        "id": 7,
        "province_en": "Sudur Paschim Province",
        "province_np": "सुदुर पश्चिम प्रदेश",
        
      },
      "district": {
        "id": 76,
        "did": 708,
        
        "district_en": "Kailali",
        "district_np": "कैलाली"
      }
    },
    {
      "id": 739,
      "lgid": 70808,
      
      "lgname_en": "Janaki Rural Mun",
      "lgname_np": "जानकी गाउँपालिका",
      "province": {
        "id": 7,
        "province_en": "Sudur Paschim Province",
        "province_np": "सुदुर पश्चिम प्रदेश",
        
      },
      "district": {
        "id": 76,
        "did": 708,
        
        "district_en": "Kailali",
        "district_np": "कैलाली"
      }
    },
    {
      "id": 740,
      "lgid": 70809,
      
      "lgname_en": "Joshipur Rural Mun",
      "lgname_np": "जोशीपुर गाउँपालिका",
      "province": {
        "id": 7,
        "province_en": "Sudur Paschim Province",
        "province_np": "सुदुर पश्चिम प्रदेश",
        
      },
      "district": {
        "id": 76,
        "did": 708,
        
        "district_en": "Kailali",
        "district_np": "कैलाली"
      }
    },
    {
      "id": 741,
      "lgid": 70810,
      
      "lgname_en": "Tikapur Municipality",
      "lgname_np": "टिकापुर नगरपालिका",
      "province": {
        "id": 7,
        "province_en": "Sudur Paschim Province",
        "province_np": "सुदुर पश्चिम प्रदेश",
        
      },
      "district": {
        "id": 76,
        "did": 708,
        
        "district_en": "Kailali",
        "district_np": "कैलाली"
      }
    },
    {
      "id": 742,
      "lgid": 70811,
      
      "lgname_en": "Bhajani Municipality",
      "lgname_np": "भजनी नगरपालिका",
      "province": {
        "id": 7,
        "province_en": "Sudur Paschim Province",
        "province_np": "सुदुर पश्चिम प्रदेश",
        
      },
      "district": {
        "id": 76,
        "did": 708,
        
        "district_en": "Kailali",
        "district_np": "कैलाली"
      }
    },
    {
      "id": 743,
      "lgid": 70812,
      
      "lgname_en": "Kailari Rural Mun",
      "lgname_np": "कैलारी गाउँपालिका",
      "province": {
        "id": 7,
        "province_en": "Sudur Paschim Province",
        "province_np": "सुदुर पश्चिम प्रदेश",
        
      },
      "district": {
        "id": 76,
        "did": 708,
        
        "district_en": "Kailali",
        "district_np": "कैलाली"
      }
    },
    {
      "id": 744,
      "lgid": 70813,
      
      "lgname_en": "Dhangadhi Sub-Metro",
      "lgname_np": "धनगढी उपमहानगरपालिका",
      "province": {
        "id": 7,
        "province_en": "Sudur Paschim Province",
        "province_np": "सुदुर पश्चिम प्रदेश",
        
      },
      "district": {
        "id": 76,
        "did": 708,
        
        "district_en": "Kailali",
        "district_np": "कैलाली"
      }
    },
    {
      "id": 745,
      "lgid": 70901,
      
      "lgname_en": "Krishnapur Municipality",
      "lgname_np": "कृष्णपुर नगरपालिका",
      "province": {
        "id": 7,
        "province_en": "Sudur Paschim Province",
        "province_np": "सुदुर पश्चिम प्रदेश",
        
      },
      "district": {
        "id": 77,
        "did": 709,
        
        "district_en": "Kanchanpur",
        "district_np": "कञ्चनपुर"
      }
    },
    {
      "id": 746,
      "lgid": 70902,
      
      "lgname_en": "Shuklaphanta Municipality",
      "lgname_np": "शुक्लाफाँटा नगरपालिका",
      "province": {
        "id": 7,
        "province_en": "Sudur Paschim Province",
        "province_np": "सुदुर पश्चिम प्रदेश",
        
      },
      "district": {
        "id": 77,
        "did": 709,
        
        "district_en": "Kanchanpur",
        "district_np": "कञ्चनपुर"
      }
    },
    {
      "id": 747,
      "lgid": 70903,
      
      "lgname_en": "Bedkot Municipality",
      "lgname_np": "वेदकोट नगरपालिका",
      "province": {
        "id": 7,
        "province_en": "Sudur Paschim Province",
        "province_np": "सुदुर पश्चिम प्रदेश",
        
      },
      "district": {
        "id": 77,
        "did": 709,
        
        "district_en": "Kanchanpur",
        "district_np": "कञ्चनपुर"
      }
    },
    {
      "id": 748,
      "lgid": 70904,
      
      "lgname_en": "Bheemdatta Municipality",
      "lgname_np": "भीमदत्त नगरपालिका",
      "province": {
        "id": 7,
        "province_en": "Sudur Paschim Province",
        "province_np": "सुदुर पश्चिम प्रदेश",
        
      },
      "district": {
        "id": 77,
        "did": 709,
        
        "district_en": "Kanchanpur",
        "district_np": "कञ्चनपुर"
      }
    },
    {
      "id": 749,
      "lgid": 70905,
      
      "lgname_en": "Mahakali Municipality",
      "lgname_np": "दोधारा चादँनी नगरपालिका",
      "province": {
        "id": 7,
        "province_en": "Sudur Paschim Province",
        "province_np": "सुदुर पश्चिम प्रदेश",
        
      },
      "district": {
        "id": 77,
        "did": 709,
        
        "district_en": "Kanchanpur",
        "district_np": "कञ्चनपुर"
      }
    },
    {
      "id": 750,
      "lgid": 70906,
      
      "lgname_en": "Laljhadi Rural Mun",
      "lgname_np": "लालझाडी गाउँपालिका",
      "province": {
        "id": 7,
        "province_en": "Sudur Paschim Province",
        "province_np": "सुदुर पश्चिम प्रदेश",
        
      },
      "district": {
        "id": 77,
        "did": 709,
        
        "district_en": "Kanchanpur",
        "district_np": "कञ्चनपुर"
      }
    },
    {
      "id": 751,
      "lgid": 70907,
      
      "lgname_en": "Punarbas Municipality",
      "lgname_np": "पुर्नवास नगरपालिका",
      "province": {
        "id": 7,
        "province_en": "Sudur Paschim Province",
        "province_np": "सुदुर पश्चिम प्रदेश",
        
      },
      "district": {
        "id": 77,
        "did": 709,
        
        "district_en": "Kanchanpur",
        "district_np": "कञ्चनपुर"
      }
    },
    {
      "id": 752,
      "lgid": 70908,
      
      "lgname_en": "Belauri Municipality",
      "lgname_np": "बेलौरी नगरपालिका",
      "province": {
        "id": 7,
        "province_en": "Sudur Paschim Province",
        "province_np": "सुदुर पश्चिम प्रदेश",
        
      },
      "district": {
        "id": 77,
        "did": 709,
        
        "district_en": "Kanchanpur",
        "district_np": "कञ्चनपुर"
      }
    },
    {
      "id": 753,
      "lgid": 70909,
      
      "lgname_en": "Beldandi Rural Mun",
      "lgname_np": "बेलडाडी गाउँपालिका",
      "province": {
        "id": 7,
        "province_en": "Sudur Paschim Province",
        "province_np": "सुदुर पश्चिम प्रदेश",
        
      },
      "district": {
        "id": 77,
        "did": 709,
        
        "district_en": "Kanchanpur",
        "district_np": "कञ्चनपुर"
      }
    }
  ]

    for x in data:
        p = Province.objects.get(pid=x["province"]["id"])
        d = District.objects.get(did=x["district"]["did"])
        l = LocalGovernment(province=p,district=d,lgid=x["lgid"],name=x["lgname_en"])
        l.save()
    queryset = LocalGovernment.objects.all()
    serializer_class = LocalGovernmentSerializer
