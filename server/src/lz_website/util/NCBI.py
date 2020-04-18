"""
NCBI相关api模块
"""
import asyncio
from tornado.httpclient import AsyncHTTPClient
import xml.etree.ElementTree  as ET
import json

class BaseNcbi(object):
    base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"
    api_key = "d6819c90815ed574654313029d1dc663e007"
    client = AsyncHTTPClient()

    def __init__(self, term):
        self.term = str(term)  #"cyanobacterial+" +

    async def esearch(self):
        """
        根据关键字得到文章的id
        :return: ["esearchresult"]["count"]:得到总数量
                 ["esearchresult"]["idlist"]:得到文章列表
        """
        esearch_url = BaseNcbi.base_url + "esearch.fcgi?db=pubmed&api_key=" + BaseNcbi.api_key + "&retmode=json&retmax=50&term=" + self.term
        print(esearch_url)
        res = await BaseNcbi.client.fetch(esearch_url)
        return json.loads(res.body.decode("utf-8"))

    async def efetch(self):
        """
        得到对应id的文章信息
        :return: 返回xml的text内容
        """
        efetch_url = BaseNcbi.base_url + "efetch.fcgi?db=pubmed&api_key=" + BaseNcbi.api_key + "&retmode=xml&id="
        idList = await self.esearch()
        idList = idList["esearchresult"]["idlist"]
        for each_list in idList:
            efetch_url = efetch_url + str(each_list) + ","
        res = await BaseNcbi.client.fetch(efetch_url)
        return res.body.decode("utf-8")

    async def getRefArticleInfo(self):
        """
        得到相关文章的列表
        :return: 返回格式[{},{},{}]
        """
        xml_text = await self.efetch()
        tree = ET.XML(xml_text)
        all_article_list = []
        all_article = tree.findall("PubmedArticle")
        for each_article in all_article:
            article_dict = {}
            try:
                pmid = each_article[0].find("PMID").text
            except:
                pmid = ' '
            try:
                title = each_article[0].find("Article").find("ArticleTitle").text
            except:
                title = ' '
            try:
                authorLastName = each_article[0].find("Article").find("AuthorList")[0].find("LastName").text
            except:
                authorLastName = ' '
            try:
                authorInitial = each_article[0].find("Article").find("AuthorList")[0].find("Initials").text
            except:
                authorInitial = ' '
            try:
                medlineTA = each_article[0].find("MedlineJournalInfo").find("MedlineTA").text
            except:
                medlineTA = ' '
            try:
                pubdate = each_article[0].find("Article").find("Journal").find("JournalIssue").find("PubDate").find(
                    "Year").text
            except:
                pubdate = ' '
            try:
                abstract = each_article[0].find("Article").find("Abstract").find("AbstractText").text
            except:
                abstract = ' '
            try:
                doi = [i.text for i in each_article.find("PubmedData").find("ArticleIdList").findall("ArticleId") if
                       i.attrib["IdType"] == 'doi'][0]
            except:
                doi = ' '
            article_dict["pmid"] = pmid
            article_dict["title"] = title
            article_dict["authorLastName"] = authorLastName
            article_dict["authorInitial"] = authorInitial
            article_dict["medlineTA"] = medlineTA
            article_dict["pubdate"] = pubdate
            if abstract is None:
                article_dict["abstract"] = "not abstract"
            else:
                article_dict["abstract"] = abstract[0:300]
            article_dict["doi"] = doi
            all_article_list.append(article_dict)
        return all_article_list


if __name__ == "__main__":
    a = BaseNcbi("123")
    loop = asyncio.get_event_loop()
    loop.run_until_complete(a.getRefArticleInfo())