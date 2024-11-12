import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useFamilyStore = defineStore('family', () => {
    const familyInfo = ref([
        {   id:crypto.randomUUID(),
            familyName: '메디치',
            father: '로도비코 데 메디치', 
            mother: '마리아 살비아티', 
            children: [ 
                        {id:crypto.randomUUID(),name: '틀레도의 엘 레오노르'}, 
                        {id:crypto.randomUUID(),name: '코시모 1세'}, 
                      ] 
            }, 
            { 
              id:crypto.randomUUID(),
              familyName: '전주 이씨',
              father: '이도', 
              mother: '소헌왕후', 
              children: [ 
                          {id:crypto.randomUUID(),name: '이향'}, 
                           {id:crypto.randomUUID(),name: '이유'}, 
                        ] 
            },
    ])
    return {
        familyInfo,
    }
})