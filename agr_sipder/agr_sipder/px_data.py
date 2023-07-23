
import scrapy

query = '''
    https://apigw.px.91app.tw/pythia-cdn/graphql?shopId=2&lang=zh-TW&query=query cms_shopCategory($shopId: Int!, $categoryId: Int!, $startIndex: Int!, $fetchCount: Int!, $orderBy: String, $isShowCurator: Boolean, $locationId: Int, $tagFilters: [ItemTagFilter], $tagShowMore: Boolean, $serviceType: String, $minPrice: Float, $maxPrice: Float, $payType: [String], $shippingType: [String]) {
  shopCategory(shopId: $shopId, categoryId: $categoryId) {
    salePageList(startIndex: $startIndex, maxCount: $fetchCount, orderBy: $orderBy, isCuratorable: $isShowCurator, locationId: $locationId, tagFilters: $tagFilters, tagShowMore: $tagShowMore, minPrice: $minPrice, maxPrice: $maxPrice, payType: $payType, shippingType: $shippingType, serviceType: $serviceType) {
      salePageList {
        title
        price
        suggestPrice
      }
      totalSize
      shopCategoryId
      shopCategoryName
      statusDef
      listModeDef
      orderByDef
      dataSource
      tags {
        isGroupShowMore
        groups {
          groupId
          groupDisplayName
          isKeyShowMore
          keys {
            keyId
            keyDisplayName
            __typename
          }
          __typename
        }
        __typename
      }
      priceRange {
        min
        max
        __typename
      }
      __typename
    }
    __typename
  }
}
&operationName=cms_shopCategory&variables={"shopId":2,"categoryId":240,"startIndex":0,"fetchCount":100,"orderBy":"","isShowCurator":true,"locationId":2094,"tagFilters":[],"tagShowMore":false}
'''

