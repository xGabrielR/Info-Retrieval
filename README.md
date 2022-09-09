# Info Retrieval
<hr>
1. With this project I will study ElasticSearch and NLP with friends using Git

![info-logo](https://user-images.githubusercontent.com/75986085/189242715-dc01435a-eb82-4999-973d-8028c338b063.png)

<h2>Summary</h2>
<hr>

- [0. Bussiness Problem](#0-bussiness-problem)
  - [0.1. What is a Law Bussiness Model](#01-what-is-a-law-bussiness-model)
    - [0.1.1. Value Proposition and Customer Segment](#011-value-proposition-and-customer-segment)
    - [0.1.2. Key Sources](#012-key-sources)
    - [0.1.3. Key Partners](#013-key-partners)
  - [0.2. Key Facts About Law](#02-key-facts-about-law)
  - [0.3. Fraud in Financial Transactions](#03-fraud-in-financial-transactions)
- [1. Solution Strategy and Assumptions Resume](#1-solution-strategy-and-assumptions-resume)
  - [1.1. First CRISP Cycle](#11-first-crisp-cycle)
  
- [9. References](#9-references)

---

<h2>0. Bussiness Problem</h2>
<hr>

<p>All data is generated on every day and currently, as all data is generated on every day and currently, as all data is generated on every day, however, all new data is generated on every day, however , not all data is generated every day, however, a lot of new information is generated every day, however, not all data is generated every day, however, a lot of new information is generated every day However, not all data is generated every day. It is not necessary to provide access to a data collection, devices accessing a data collection, and other configuration devices that provide access to a data collection, and other configuration devices that provide access to a data collection, and so on. configuration devices that provide access to a data collection, and other configuration devices to provide data collection, and other configuration devices that provide access to a data collection.</p>
<p>The important thing is access to these implications, in this sense, there are important implications, they are.</p>

> *1.* Need for different sources that may not be perceptible or not bring visible information and waste of time.
>
> *2.* Failure to read or interpret these specifics.
>
> *3.* Unproductive work due to several factors already mentioned above.

<p>How would you go about helping these institutions that need this data using the knowledge you already know in order to develop an end-to-end solution to be able to develop and complete this demand?</p>

<h3>0.1. What is a Law Bussiness Model</h3>

<p>Basically there are four main types for this business model.</p>

**Boutique Office** 
This is a business model in which professionals are highly specialized. Thus, in this format, there is a search for recognition in the market and, as a consequence, the causes of higher value. In the case of a boutique office, the service is more exclusive and, normally, there are a smaller number of clients when compared to a simple office. In this way, the service is much more personalized.

**Mass Advocacy** 
In this business model, the firm deals with a much larger volume of cases. Unlike the boutique firm, the mass law business model focuses on simpler cases, which allows it to serve more clients. However, unlike the simple office, in this business model there is standardization and a more organized search for new clients.

**Outsourcing Advocacy** 
Small and medium businesses need legal support. However, often internalizing this type of service can be costly. This is where the outsourcing business model comes in. Thus, professionals serve companies in an outsourced manner, focusing on demands ranging from civil, administrative or labor areas.

**Advocacy Web Service**
In the case of a business model for web service law, the service takes place online. Thus, this greatly expands the scope of the office in receiving cases from different audiences. However, without a digital office strategy, web service can become inefficient.

<p>There are several ways to understand a law firm's business model or even try to build a similar model. with some tools. I will briefly mention some important concepts of this business model that I discovered from some research based on the business model canvas. Bussiness Model Canvas is a good visual way to unravel your law business model, but there are other analytical tools for this process.</p>

<h4>0.1.1. Value Proposition and Customer Segment</h4>
<p>Undoubtedly, the most important part of the business canvas is the customer segment and the value proposition, in short, what my company does that differentiates it from competitors and which customers benefit from the activities that the company performs.</p>

<h4>0.1.2. Key Sources</h4>
<p>To exercise a position of this magnitude, the professional can be trained in several areas, for example, with technology, dedicated to labor legislation, or a professional dedicated to high-risk analysis work, such as fraud or lawsuits involving medicine and even as wills and constitutive. articles for the mass market. Undoubtedly, knowledge in certain areas is an important part of the business canvas.</p>

<h4>0.1.3. Key Partners</h4>
<p>Most law firms work in the partnership model. Some partners provide seed capital to the company. Contract lawyers generate revenue for the firm by charging clients a flat fee for their work, and partners increase their profits by hiring more associates to generate more billable hours. There are also partnerships with third parties so as not to overload the company's internal professionals, these outsourced workers.</p>


<h3>0.2. Key Facts About Law</h3>

<p>According to some sources, lawyers will witness a crisis where law and law courses will be more commonplace and in addition to a clear competitiveness in the job market to exercise the position for this profession. According to data from Oab, the exponential growth in the number of lawyers creates today in Brazil a series of employability problems and those who are already employed performing their duties end up being servants of the country's large offices.</p>

<p>Elder Nogueira states that, "The democratization of law is the urgent way to change the situation, if this does not happen, in the near future we will be putting on the market an immense number of professionals with the label of failure for choosing the wrong course".</p>

<p>According to the Federal Constitution of 1988, the most important document in Brazil, mentions that the lawyer is indispensable to the administration of justice, without the lawyer there is no way to achieve justice.</p>

<p>Startups and large companies are using machine learning to dig up evidence, recognize clauses, identify anomalies, compare decisions and other data-intensive tasks.</p>

 
<h2>1. Solution Strategy and Assumptions Resume</h2>
<hr>

<p>The first ideia is make a scrapy process to collect data from source and store on a simple database to retrieve from a webapp.</p>
<p>After planning, the initial idea was redone based on the result of the first development cycle. It was then replanned together again, but one of those involved left the project, so we continue studying and developing the parts and pieces after the results of the first cycle.</p>
<p>The first problem is the quality of the sites for Scrapy, low html and hard to clean a massive text.</p>
<p>After some study, the team selected Elasticsearch because the Sql database do not work weel based on big amount of text for some laws.</p>

<h3>1.1. Firstand Second CRISP Cycle</h3>

<ul>
  <dl>
    <dt>Data Scrapy from sites.</dt>
      <dd>This is the first step on coding time, in thisstep the team im parallel make try to make a Scrapy and using NLTK (tool used to clean the data that was mentioned in the planning).</p>
    <dt>ETL Processand and SQL Study.</dt>
      <dd>I developeda ETL process on the first scrapy script using Prefect cloud and Rundeck to start the process, and the another partners start study SQL and Elasticsearch for data.</dt>
      <dd>In thsi step, of those involved left. ;-;</dd>
    <dt>Data Deploy on Elastic and Kibana Study.</dt>
      <dd>Great tools Require big responsibilities, so the team was involved in studying Elastic tools.</dd>
  </dl>
</ul>

<h3>1.2. Third CRISP Cycle</h3>

<ul>
  <dl>
    <dt>Cloud Infrastructure.</dt>
      <dd>After the scrapy of CF88 and CLT from sites, i have make the webapp for searches and make a simple cloud infrastructure to support the application and the database, In parallel the team used Kibana, Elasticsearch and Log's Beat based on Docker elastic stack image adn elastic cloud, for final infra I choose the cloudclusters for Elasticsearch and Heroku for Webapp.</p>
    <dt>ETL Processand.</dt>
      <dd>I have make two Scripts (CF88 and CLT scrapy) and using Rundeck, the scripts have been scheduled.</dt>
      <dd>In thsi step, of those involved left. ;-;</dd>
  </dl>
</ul>

<h2>2. Final Infrastructure</h2>
<hr>

<p>To register in the documentation of the simple infrastructure, I made a diagram to illustrate the idea, below are the results.</p>

![l](https://user-images.githubusercontent.com/75986085/189260758-cc09fd42-3627-4044-ab0f-5447f5bfbb6f.png)


<h2>3. Info Law App!</h2>
<hr>

<p>Finally, the Webapp, this app is made with Stramlit python framework and deploy in a simple docker container atHeroku container cloud.</p>

https://user-images.githubusercontent.com/75986085/189261422-8ad350bf-c3c6-4b67-b344-09eeaf953fa9.mp4


<h2>4. References</h2>
<hr>

<ul>
  <li><a href="https://elderns.jusbrasil.com.br/artigos/706794291/a-realidade-da-advocacia-no-brasil-precisamos-conversar-sobre-o-assunto">Uma realidade dos advogados no Brasil.</a></li>
  <li><a href="https://blog.sajadv.com.br/modelo-de-negocio-na-advocacia/">Modelo de negócio de Advocacia.</a></li>
  <li><a href="https://smallbusiness.chron.com/transactional-firm-36200.html">Law Firm.</a></li>
  <li><a href="https://www.youtube.com/watch?v=ZTFiql59tDY&t=10s">Exemplo do Model Canvas Canvas no ambiente jurídico.</a></li>
  <li><a href="https://blog.dsacademy.com.br/machine_learning_para_advogados/">M.L para Advocacía.</a></li>
</ul>
