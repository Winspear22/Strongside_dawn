import json
import os

# FULL translations matching the English source word-for-word (no summaries)

translations = {
    "pt-PT": {
        "contact": { "title": "Contactos", "back": "Voltar" },
        "cgv": {
            "title": "Termos e Condições Gerais de Venda", "back": "Voltar", "lastUpdate": "TC atualizados em 16/12/2025",
            "sections": {
                "preliminary": { "title": "Artigo Preliminar", "text": "Estes termos e condições gerais de venda são acordados entre a STRONGSIDE Technologies, operada por Adam Aloui, doravante designada 'o Vendedor', e qualquer pessoa que deseje efetuar uma compra através do site https://www.strongside.tech/, doravante designada 'o Comprador'." },
                "object": {
                    "title": "Artigo 1. Objeto",
                    "text1": "O objetivo destas condições gerais de venda é definir a relação contratual entre a STRONGSIDE Technologies e o Comprador, bem como as condições aplicáveis a qualquer compra efetuada através do site https://www.strongside.tech/.",
                    "text2": "A compra de um produto através deste site implica a aceitação sem reservas pelo Comprador destas condições gerais de venda, as quais reconhece ter lido antes de efetuar a sua encomenda.",
                    "text3": "Antes de qualquer transação, o Comprador declara ter plena capacidade legal para se vincular a estas condições gerais de venda.",
                    "text4": "A STRONGSIDE Technologies reserva-se o direito de modificar estas condições gerais de venda a qualquer momento para cumprir com novas regulamentações ou para melhorar a utilização do seu site. As condições aplicáveis serão as que estiverem em vigor na data da encomenda."
                },
                "products": {
                    "title": "Artigo 2. Produtos",
                    "text1": "Os produtos oferecidos são aqueles listados no site https://www.strongside.tech/, sujeitos à disponibilidade. A STRONGSIDE Technologies reserva-se o direito de modificar a gama de produtos a qualquer momento.",
                    "text2": "Cada produto é apresentado no site com uma descrição das suas principais características técnicas. As fotografias são o mais precisas possível, mas não vinculam o Vendedor."
                },
                "prices": {
                    "title": "Artigo 3. Preços",
                    "text1": "Os preços apresentados nas páginas dos produtos são em euros (€), incluindo todos os impostos (IVA) aplicáveis na data da encomenda.",
                    "text2": "A STRONGSIDE Technologies reserva-se o direito de modificar os seus preços a qualquer momento, entendendo-se que o preço apresentado no momento da encomenda será o único aplicável ao Comprador.",
                    "text3": "Os preços apresentados não incluem os custos de entrega, que são cobrados separadamente com base no valor total da encomenda e no destino."
                },
                "order": {
                    "title": "Artigo 4. Encomenda e Pagamento",
                    "text1": "Antes de qualquer encomenda, o Comprador deve criar uma conta no site https://www.strongside.tech/.",
                    "paymentMethods": "Os métodos de pagamento aceites são:",
                    "method_card": "Cartão de crédito",
                    "method_paypal": "PayPal",
                    "method_transfer": "Transferência bancária",
                    "method_other": "Qualquer outro método de pagamento oferecido no site no momento da encomenda",
                    "text2": "A validação da encomenda implica a aceitação plena e completa destas condições gerais de venda.",
                    "text3": "Uma confirmação de encomenda será enviada por email ao Comprador."
                },
                "ownership": { "title": "Artigo 5. Reserva de Propriedade", "text": "A STRONGSIDE Technologies mantém a propriedade total dos produtos vendidos até ao pagamento integral do preço, incluindo taxas e impostos." },
                "returns": {
                    "title": "Artigo 6. Direito de Retratação e Devoluções",
                    "text1": "De acordo com a legislação aplicável, o Comprador dispõe de catorze (14) dias a partir da receção da sua encomenda para exercer o seu direito de retratação.",
                    "highlight": "As devoluções são aceites no prazo de 14 dias.",
                    "text2": "Os produtos devem ser devolvidos no seu estado original, não utilizados e na sua embalagem original.",
                    "text3": "Os custos de devolução são da responsabilidade do Comprador.",
                    "text4": "O reembolso será efetuado após a receção e verificação dos produtos devolvidos."
                },
                "delivery": {
                    "title": "Artigo 7. Entrega",
                    "text1": "As entregas são efetuadas na morada indicada no momento da encomenda.",
                    "text2": "Os prazos de entrega são indicativos. Em caso de atraso superior a trinta (30) dias, o Comprador pode solicitar o cancelamento da encomenda e o reembolso.",
                    "text3": "O risco de transporte é transferido para o Comprador no momento da entrega da encomenda ao transportador."
                },
                "warranty": {
                    "title": "Artigo 8. Garantia",
                    "text1": "Todos os produtos beneficiam das garantias legais de conformidade e de defeitos ocultos, conforme previsto nos artigos do Código Civil.",
                    "text2": "Qualquer reclamação, pedido de troca ou reembolso deve ser efetuado por email ou correio no prazo de trinta (30) dias após a entrega."
                },
                "liability": { "title": "Artigo 9. Responsabilidade", "text": "A STRONGSIDE Technologies não pode ser responsabilizada por danos resultantes da utilização da Internet, tais como perda de dados, intrusão, vírus ou interrupção do serviço." },
                "ip": {
                    "title": "Artigo 10. Propriedade Intelectual",
                    "text1": "Todos os elementos do site https://www.strongside.tech/ são e permanecem propriedade intelectual exclusiva da STRONGSIDE Technologies.",
                    "text2": "Qualquer reprodução, exploração ou utilização, mesmo que parcial, sem autorização prévia é estritamente proibida."
                },
                "data": {
                    "title": "Artigo 11. Dados Pessoais",
                    "text1": "A STRONGSIDE Technologies compromete-se a preservar a confidencialidade das informações pessoais fornecidas pelo Comprador.",
                    "text2": "De acordo com a Lei de Proteção de Dados e o RGPD, o Comprador tem o direito de aceder, retificar e eliminar os seus dados pessoais."
                },
                "disputes": {
                    "title": "Artigo 12. Resolução de Litígios",
                    "text1": "Estas condições gerais de venda regem-se pela lei francesa.",
                    "text2": "Em caso de litígio, será procurada uma solução amigável antes de qualquer ação judicial. Na falta desta, os tribunais competentes serão os do domicílio do réu ou do local de entrega."
                },
                "entirety": { "title": "Artigo 13. Integridade", "text": "Se alguma cláusula destas condições gerais de venda for declarada nula, as restantes cláusulas manterão a sua plena validade." },
                "duration": { "title": "Artigo 14. Duração", "text": "Estas condições aplicam-se durante toda a duração dos serviços online oferecidos pela STRONGSIDE Technologies." },
                "proof": { "title": "Artigo 15. Prova", "text": "Os registos informatizados conservados nos sistemas informáticos da STRONGSIDE Technologies constituirão prova das comunicações, encomendas e pagamentos entre as partes." }
            }
        },
        "legal": {
            "title": "Aviso Legal", "back": "Voltar", "lastUpdate": "Aviso legal atualizado em 15/12/2025",
            "sections": {
                "identification": {
                    "title": "Identificação e Publicação",
                    "editor": "Editor",
                    "editorText": "Este site é publicado por ADAM ALOUI – STRONGSIDE Technologies.",
                    "director": "Diretor de Publicação: Adam Aloui",
                    "host": "Alojamento",
                    "hostText": "Este site é alojado pela Vercel Inc., 340 S Lemon Ave #4133, Walnut, CA 91789, EUA."
                },
                "ip": {
                    "title": "Propriedade Intelectual",
                    "protection": "Todos os elementos gráficos, a estrutura e, mais geralmente, o conteúdo do site da STRONGSIDE Technologies estão protegidos por direitos de autor, direito de marcas e direitos de design.",
                    "privateUse": "Qualquer pessoa que recolha ou descarregue conteúdo ou informações do site tem apenas um direito de uso privado, pessoal e intransmissível.",
                    "reproduction": "A reprodução de uma página do site num contexto externo à STRONGSIDE ou a inserção de uma página pertencente à STRONGSIDE na página de outro site é proibida.",
                    "sanctions": "Do mesmo modo, qualquer reprodução ou representação do site, total ou parcial, é proibida sem o consentimento por escrito da STRONGSIDE e constituiria uma contrafação punível ao abrigo das leis de propriedade intelectual aplicáveis.",
                    "paperReproduction": "Textos, gráficos, desenhos, logótipos e fotos publicados pela STRONGSIDE podem ser reproduzidos em papel ou suportes eletrónicos, desde que o nome e a morada do site sejam citados e não seja feito uso comercial.",
                    "infringement": "O incumprimento das disposições acima pode constituir uma contrafação que implique a responsabilidade civil ou criminal do autor.",
                    "hyperlink": "A criação de uma hiperligação para o site www.strongside.tech só pode ser feita com a autorização da STRONGSIDE, e desde que não possa existir confusão na mente dos utilizadores quanto à identidade do site ou à origem das informações."
                },
                "data": {
                    "title": "Proteção de Dados e Cookies",
                    "intro": "Utilizamos tecnologias de rastreio para melhorar a sua experiência e analisar como o nosso site é utilizado.",
                    "ga4Title": "Google Analytics 4",
                    "ga4Text": "Utilizamos o Google Analytics 4 para compreender como os visitantes interagem com o nosso site. Estes dados são anonimizados e ajudam-nos a otimizar a sua experiência de navegação. Não são recolhidas informações de identificação pessoal.",
                    "shopifyTitle": "Shopify",
                    "shopifyText": "As transações de pagamento são geridas de forma segura pela Shopify Payments. Durante o processo de checkout, a Shopify pode recolher informações necessárias para processar a sua encomenda (nome, morada, email, informações de pagamento) de acordo com a sua política de privacidade.",
                    "vercelTitle": "Vercel Analytics",
                    "vercelText": "O nosso fornecedor de alojamento Vercel recolhe dados de desempenho anonimizados para otimizar a velocidade do site.",
                    "consent": "Ao continuar a utilizar este site, consente a utilização destas tecnologias de rastreio."
                }
            }
        }
    },
    "pt-BR": {
        "contact": { "title": "Contato", "back": "Voltar" },
        "cgv": {
            "title": "Termos e Condições Gerais de Venda", "back": "Voltar", "lastUpdate": "TC atualizados em 16/12/2025",
            "sections": {
                "preliminary": { "title": "Artigo Preliminar", "text": "Estes termos e condições gerais de venda são acordados entre a STRONGSIDE Technologies, operada por Adam Aloui, doravante denominada 'o Vendedor', e qualquer pessoa que deseje efetuar uma compra através do site https://www.strongside.tech/, doravante denominada 'o Comprador'." },
                "object": {
                    "title": "Artigo 1. Objeto",
                    "text1": "O objetivo destas condições gerais de venda é definir a relação contratual entre a STRONGSIDE Technologies e o Comprador, bem como as condições aplicáveis a qualquer compra efetuada através do site https://www.strongside.tech/.",
                    "text2": "A compra de um produto através deste site implica a aceitação sem reservas pelo Comprador destas condições gerais de venda, as quais reconhece ter lido antes de efetuar o seu pedido.",
                    "text3": "Antes de qualquer transação, o Comprador declara ter plena capacidade legal para se vincular a estas condições gerais de venda.",
                    "text4": "A STRONGSIDE Technologies reserva-se o direito de modificar estas condições gerais de venda a qualquer momento para cumprir com novas regulamentações ou para melhorar a utilização do seu site. As condições aplicáveis serão as que estiverem em vigor na data do pedido."
                },
                "products": {
                    "title": "Artigo 2. Produtos",
                    "text1": "Os produtos oferecidos são aqueles listados no site https://www.strongside.tech/, sujeitos à disponibilidade. A STRONGSIDE Technologies reserva-se o direito de modificar a gama de produtos a qualquer momento.",
                    "text2": "Cada produto é apresentado no site com uma descrição das suas principais características técnicas. As fotografias são o mais precisas possível, mas não vinculam o Vendedor."
                },
                "prices": {
                    "title": "Artigo 3. Preços",
                    "text1": "Os preços apresentados nas páginas dos produtos são em euros (€), incluindo todos os impostos (IVA) aplicáveis na data do pedido.",
                    "text2": "A STRONGSIDE Technologies reserva-se o direito de modificar os seus preços a qualquer momento, entendendo-se que o preço apresentado no momento do pedido será o único aplicável ao Comprador.",
                    "text3": "Os preços apresentados não incluem os custos de entrega, que são cobrados separadamente com base no valor total do pedido e no destino."
                },
                "order": {
                    "title": "Artigo 4. Pedido e Pagamento",
                    "text1": "Antes de qualquer pedido, o Comprador deve criar uma conta no site https://www.strongside.tech/.",
                    "paymentMethods": "Os métodos de pagamento aceitos são:",
                    "method_card": "Cartão de crédito",
                    "method_paypal": "PayPal",
                    "method_transfer": "Transferência bancária",
                    "method_other": "Qualquer outro método de pagamento oferecido no site no momento do pedido",
                    "text2": "A validação do pedido implica a aceitação plena e completa destas condições gerais de venda.",
                    "text3": "Uma confirmação de pedido será enviada por e-mail ao Comprador."
                },
                "ownership": { "title": "Artigo 5. Reserva de Propriedade", "text": "A STRONGSIDE Technologies mantém a propriedade total dos produtos vendidos até ao pagamento integral do preço, incluindo taxas e impostos." },
                "returns": {
                    "title": "Artigo 6. Direito de Arrependimento e Devoluções",
                    "text1": "De acordo com a legislação aplicável, o Comprador dispõe de catorze (14) dias a partir do recebimento do seu pedido para exercer o seu direito de arrependimento.",
                    "highlight": "As devoluções são aceitas no prazo de 14 dias.",
                    "text2": "Os produtos devem ser devolvidos no seu estado original, não utilizados e na sua embalagem original.",
                    "text3": "Os custos de devolução são de responsabilidade do Comprador.",
                    "text4": "O reembolso será efetuado após o recebimento e verificação dos produtos devolvidos."
                },
                "delivery": {
                    "title": "Artigo 7. Entrega",
                    "text1": "As entregas são efetuadas no endereço indicado no momento do pedido.",
                    "text2": "Os prazos de entrega são indicativos. Em caso de atraso superior a trinta (30) dias, o Comprador pode solicitar o cancelamento do pedido e o reembolso.",
                    "text3": "O risco de transporte é transferido para o Comprador no momento da entrega do pacote ao transportador."
                },
                "warranty": {
                    "title": "Artigo 8. Garantia",
                    "text1": "Todos os produtos beneficiam das garantias legais de conformidade e de defeitos ocultos, conforme previsto nos artigos do Código Civil.",
                    "text2": "Qualquer reclamação, pedido de troca ou reembolso deve ser efetuado por e-mail ou correio no prazo de trinta (30) dias após a entrega."
                },
                "liability": { "title": "Artigo 9. Responsabilidade", "text": "A STRONGSIDE Technologies não pode ser responsabilizada por danos resultantes da utilização da Internet, tais como perda de dados, intrusão, vírus ou interrupção do serviço." },
                "ip": {
                    "title": "Artigo 10. Propriedade Intelectual",
                    "text1": "Todos os elementos do site https://www.strongside.tech/ são e permanecem propriedade intelectual exclusiva da STRONGSIDE Technologies.",
                    "text2": "Qualquer reprodução, exploração ou utilização, mesmo que parcial, sem autorização prévia é estritamente proibida."
                },
                "data": {
                    "title": "Artigo 11. Dados Pessoais",
                    "text1": "A STRONGSIDE Technologies compromete-se a preservar a confidencialidade das informações pessoais fornecidas pelo Comprador.",
                    "text2": "De acordo com a Lei de Proteção de Dados e o RGPD/LGPD, o Comprador tem o direito de acessar, retificar e eliminar seus dados pessoais."
                },
                "disputes": {
                    "title": "Artigo 12. Resolução de Disputas",
                    "text1": "Estas condições gerais de venda regem-se pela lei francesa.",
                    "text2": "Em caso de disputa, será procurada uma solução amigável antes de qualquer ação judicial. Na falta desta, os tribunais competentes serão os do domicílio do réu ou do local de entrega."
                },
                "entirety": { "title": "Artigo 13. Integridade", "text": "Se alguma cláusula destas condições gerais de venda for declarada nula, as restantes cláusulas manterão a sua plena validade." },
                "duration": { "title": "Artigo 14. Duração", "text": "Estas condições aplicam-se durante toda a duração dos serviços online oferecidos pela STRONGSIDE Technologies." },
                "proof": { "title": "Artigo 15. Prova", "text": "Os registros informatizados conservados nos sistemas de computador da STRONGSIDE Technologies constituirão prova das comunicações, pedidos e pagamentos entre as partes." }
            }
        },
        "legal": {
            "title": "Aviso Legal", "back": "Voltar", "lastUpdate": "Aviso legal atualizado em 15/12/2025",
            "sections": {
                "identification": {
                    "title": "Identificação e Publicação",
                    "editor": "Editor",
                    "editorText": "Este site é publicado por ADAM ALOUI – STRONGSIDE Technologies.",
                    "director": "Diretor de Publicação: Adam Aloui",
                    "host": "Hospedagem",
                    "hostText": "Este site é hospedado pela Vercel Inc., 340 S Lemon Ave #4133, Walnut, CA 91789, EUA."
                },
                "ip": {
                    "title": "Propriedade Intelectual",
                    "protection": "Todos os elementos gráficos, a estrutura e, mais geralmente, o conteúdo do site da STRONGSIDE Technologies estão protegidos por direitos de autor, direito de marcas e direitos de design.",
                    "privateUse": "Qualquer pessoa que colete ou baixe conteúdo ou informações do site tem apenas um direito de uso privado, pessoal e intransferível.",
                    "reproduction": "A reprodução de uma página do site num contexto externo à STRONGSIDE ou a inserção de uma página pertencente à STRONGSIDE na página de outro site é proibida.",
                    "sanctions": "Do mesmo modo, qualquer reprodução ou representação do site, total ou parcial, é proibida sem o consentimento por escrito da STRONGSIDE e constituiria uma contrafação punível ao abrigo das leis de propriedade intelectual aplicáveis.",
                    "paperReproduction": "Textos, gráficos, desenhos, logotipos e fotos publicados pela STRONGSIDE podem ser reproduzidos em papel ou suportes eletrônicos, desde que o nome e o endereço do site sejam citados e não seja feito uso comercial.",
                    "infringement": "O descumprimento das disposições acima pode constituir uma contrafação que implique a responsabilidade civil ou criminal do autor.",
                    "hyperlink": "A criação de um hiperlink para o site www.strongside.tech só pode ser feita com a autorização da STRONGSIDE, e desde que não possa existir confusão na mente dos usuários quanto à identidade do site ou à origem das informações."
                },
                "data": {
                    "title": "Proteção de Dados e Cookies",
                    "intro": "Utilizamos tecnologias de rastreamento para melhorar a sua experiência e analisar como o nosso site é utilizado.",
                    "ga4Title": "Google Analytics 4",
                    "ga4Text": "Utilizamos o Google Analytics 4 para compreender como os visitantes interagem com o nosso site. Estes dados são anonimizados e ajudam-nos a otimizar a sua experiência de navegação. Não são coletadas informações de identificação pessoal.",
                    "shopifyTitle": "Shopify",
                    "shopifyText": "As transações de pagamento são gerenciadas de forma segura pela Shopify Payments. Durante o processo de checkout, a Shopify pode coletar informações necessárias para processar o seu pedido (nome, endereço, e-mail, informações de pagamento) de acordo com a sua política de privacidade.",
                    "vercelTitle": "Vercel Analytics",
                    "vercelText": "O nosso provedor de hospedagem Vercel coleta dados de desempenho anonimizados para otimizar a velocidade do site.",
                    "consent": "Ao continuar a utilizar este site, você consente a utilização destas tecnologias de rastreamento."
                }
            }
        }
    },
    "sv": {
        "contact": { "title": "Kontakta oss", "back": "Tillbaka" },
        "cgv": {
            "title": "Allmänna Försäljningsvillkor",
            "back": "Tillbaka",
            "lastUpdate": "Uppdaterad 2025-12-16",
            "sections": {
                "preliminary": {
                    "title": "Inledning",
                    "text": "Dessa allmänna försäljningsvillkor ingås mellan STRONGSIDE Technologies, driven av Adam Aloui, hädanefter kallad 'Säljaren', som driver webbplatsen https://www.strongside.tech/, och varje fysisk eller juridisk person som önskar göra ett köp via webbplatsen https://www.strongside.tech/, hädanefter kallad 'Köparen'."
                },
                "object": {
                    "title": "Artikel 1. Syfte",
                    "text1": "Syftet med dessa allmänna försäljningsvillkor är att definiera det avtalsmässiga förhållandet mellan STRONGSIDE Technologies och Köparen, samt de villkor som gäller för alla köp som görs via webbplatsen https://www.strongside.tech/.",
                    "text2": "Köp av en produkt via denna webbplats innebär Köparens oinskränkta godkännande av dessa allmänna försäljningsvillkor, vilka Köparen intygar att ha läst innan beställningen görs.",
                    "text3": "Före varje transaktion förklarar Köparen att hen har full rättslig kapacitet att binda sig till dessa allmänna försäljningsvillkor.",
                    "text4": "STRONGSIDE Technologies förbehåller sig rätten att när som helst ändra dessa allmänna försäljningsvillkor för att följa nya regler eller för att förbättra användningen av sin webbplats. De tillämpliga villkoren är de som gäller vid datumet för beställningen."
                },
                "products": {
                    "title": "Artikel 2. Produkter",
                    "text1": "De produkter som erbjuds är de som finns listade på webbplatsen https://www.strongside.tech/, i mån av tillgång. STRONGSIDE Technologies förbehåller sig rätten att när som helst ändra produktsortimentet.",
                    "text2": "Varje produkt presenteras på webbplatsen med en beskrivning av dess huvudsakliga tekniska egenskaper. Bilderna är så exakta som möjligt men är inte bindande för Säljaren."
                },
                "prices": {
                    "title": "Artikel 3. Priser",
                    "text1": "Priserna som visas på produktsidorna är i euro (€), inklusive alla skatter (moms) som gäller på beställningsdagen.",
                    "text2": "STRONGSIDE Technologies förbehåller sig rätten att när som helst ändra sina priser, men det pris som visas vid beställningstillfället är det enda som gäller för Köparen.",
                    "text3": "De visade priserna inkluderar inte leveranskostnader, vilka debiteras separat baserat på det totala beställningsbeloppet och destinationen."
                },
                "order": {
                    "title": "Artikel 4. Beställning och Betalning",
                    "text1": "Innan någon beställning görs måste Köparen skapa ett konto på webbplatsen https://www.strongside.tech/.",
                    "paymentMethods": "Accepterade betalningsmetoder är:",
                    "method_card": "Kreditkort",
                    "method_paypal": "PayPal",
                    "method_transfer": "Banköverföring",
                    "method_other": "Varje annan betalningsmetod som erbjuds på webbplatsen vid beställningstillfället",
                    "text2": "Bekräftelse av beställningen innebär fullständigt och oinskränkt godkännande av dessa allmänna försäljningsvillkor.",
                    "text3": "En orderbekräftelse kommer att skickas via e-post till Köparen."
                },
                "ownership": {
                    "title": "Artikel 5. Äganderättsförbehåll",
                    "text": "STRONGSIDE Technologies behåller full äganderätt till de sålda produkterna tills full betalning av priset, inklusive avgifter och skatter, har erlagts."
                },
                "returns": {
                    "title": "Artikel 6. Ångerrätt och Returer",
                    "text1": "I enlighet med tillämplig lagstiftning har Köparen fjorton (14) dagar från mottagandet av sin beställning på sig att utöva sin ångerrätt.",
                    "highlight": "Returer accepteras inom 14 dagar.",
                    "text2": "Produkter måste returneras i sitt ursprungliga skick, oanvända och i originalförpackningen.",
                    "text3": "Returkostnader bekostas av Köparen.",
                    "text4": "Återbetalning sker efter mottagande och kontroll av de returnerade produkterna."
                },
                "delivery": {
                    "title": "Artikel 7. Leverans",
                    "text1": "Leveranser sker till den adress som anges vid beställningstillfället.",
                    "text2": "Leveranstider är ungefärliga. Vid försening som överstiger trettio (30) dagar kan Köparen begära att beställningen annulleras och återbetalas.",
                    "text3": "Transportrisken övergår till Köparen vid överlämning av paketet till transportören."
                },
                "warranty": {
                    "title": "Artikel 8. Garanti",
                    "text1": "Alla produkter omfattas av lagstadgade garantier om överensstämmelse och dolda fel enligt gällande lagstiftning.",
                    "text2": "Varje reklamation, begäran om byte eller återbetalning måste göras via e-post eller post inom trettio (30) dagar efter leverans."
                },
                "liability": {
                    "title": "Artikel 9. Ansvar",
                    "text": "STRONGSIDE Technologies kan inte hållas ansvarigt för skador som uppstår till följd av användning av Internet, såsom dataförlust, intrång, virus eller tjänsteavbrott."
                },
                "ip": {
                    "title": "Artikel 10. Immaterialrätt",
                    "text1": "Alla element på webbplatsen https://www.strongside.tech/ är och förblir exklusiv immateriell egendom tillhörande STRONGSIDE Technologies.",
                    "text2": "All reproduktion, exploatering eller användning, även delvis, utan föregående tillstånd är strängt förbjuden."
                },
                "data": {
                    "title": "Artikel 11. Personuppgifter",
                    "text1": "STRONGSIDE Technologies åtar sig att bevara sekretessen för personlig information som lämnas av Köparen.",
                    "text2": "I enlighet med dataskyddslagar och GDPR har Köparen rätt att få tillgång till, rätta och radera sina personuppgifter."
                },
                "disputes": {
                    "title": "Artikel 12. Tvistlösning",
                    "text1": "Dessa allmänna försäljningsvillkor styrs av fransk lag.",
                    "text2": "Vid tvist kommer en minlig lösning att sökas innan någon rättslig åtgärd vidtas. I annat fall kommer behöriga domstolar att vara de vid svarandens hemvist eller leveransorten."
                },
                "entirety": {
                    "title": "Artikel 13. Fullständighet",
                    "text": "Om någon klausul i dessa allmänna försäljningsvillkor förklaras ogiltig, kommer de övriga klausulerna att behålla sin fulla giltighet."
                },
                "duration": {
                    "title": "Artikel 14. Varaktighet",
                    "text": "Dessa villkor gäller under hela varaktigheten av de onlinetjänster som erbjuds av STRONGSIDE Technologies."
                },
                "proof": {
                    "title": "Artikel 15. Bevis",
                    "text": "De datoriserade register som förvaras i STRONGSIDE Technologies datorsystem kommer att utgöra bevis på kommunikation, beställningar och betalningar mellan parterna."
                }
            }
        },
        "legal": {
            "title": "Juridisk Information",
            "back": "Tillbaka",
            "lastUpdate": "Juridisk information uppdaterad 2025-12-15",
            "sections": {
                "identification": {
                    "title": "Identifikation och Publicering",
                    "editor": "Utgivare",
                    "editorText": "Denna webbplats publiceras av ADAM ALOUI – STRONGSIDE Technologies.",
                    "director": "Ansvarig utgivare: Adam Aloui",
                    "host": "Webbhotell",
                    "hostText": "Denna webbplats hostas av Vercel Inc., 340 S Lemon Ave #4133, Walnut, CA 91789, USA."
                },
                "ip": {
                    "title": "Immaterialrätt",
                    "protection": "Alla grafiska element, struktur och mer generellt innehållet på STRONGSIDE Technologies webbplats är skyddade av upphovsrätt, varumärkesrätt och designrättigheter.",
                    "privateUse": "Alla som samlar in eller laddar ner innehåll eller information från webbplatsen har endast en privat, personlig och icke-överlåtbar nyttjanderätt.",
                    "reproduction": "Reproduktion av en sida på webbplatsen i ett sammanhang utanför STRONGSIDE eller införande av en sida som tillhör STRONGSIDE på en annan webbplats sida är förbjuden.",
                    "sanctions": "På samma sätt är all reproduktion eller representation av webbplatsen helt eller delvis förbjuden utan skriftligt medgivande från STRONGSIDE och skulle utgöra ett intrång som är straffbart enligt tillämpliga lagar om immateriell egendom.",
                    "paperReproduction": "Texter, grafik, ritningar, logotyper och foton publicerade av STRONGSIDE får reproduceras på papper eller elektroniska medier, förutsatt att namnet och adressen till webbplatsen anges och att ingen kommersiell användning sker.",
                    "infringement": "Underlåtenhet att följa ovanstående bestämmelser kan utgöra ett intrång som medför civilrättsligt eller straffrättsligt ansvar för upphovsmannen.",
                    "hyperlink": "Skapande av en hypertextlänk till webbplatsen www.strongside.tech får endast ske med tillstånd från STRONGSIDE, och förutsatt att ingen förvirring kan uppstå hos användarna om webbplatsens identitet eller informationens ursprung."
                },
                "data": {
                    "title": "Dataskydd och Cookies",
                    "intro": "Vi använder spårningsteknik för att förbättra din upplevelse och analysera hur vår webbplats används.",
                    "ga4Title": "Google Analytics 4",
                    "ga4Text": "Vi använder Google Analytics 4 för att förstå hur besökare interagerar med vår webbplats. Dessa data är anonymiserade och hjälper oss att optimera din surfupplevelse. Ingen personligt identifierbar information samlas in.",
                    "shopifyTitle": "Shopify",
                    "shopifyText": "Betalningstransaktioner hanteras säkert av Shopify Payments. Under utcheckningsprocessen kan Shopify samla in information som är nödvändig för att behandla din beställning (namn, adress, e-post, betalningsinformation) i enlighet med deras integritetspolicy.",
                    "vercelTitle": "Vercel Analytics",
                    "vercelText": "Vår hosting-leverantör Vercel samlar in anonymiserade prestandadata för att optimera webbplatsens hastighet.",
                    "consent": "Genom att fortsätta använda denna webbplats samtycker du till användningen av dessa spårningstekniker."
                }
            }
        }
    }
}

locales_dir = 'dawn/locales'

for lang_code, translation_content in translations.items():
    file_path = os.path.join(locales_dir, f"{lang_code}.json")
    
    if os.path.exists(file_path):
        print(f"Overwriting {lang_code} with FULL content...")
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            if 'strongside' not in data:
                data['strongside'] = {}
                
            data['strongside']['legal_pages'] = translation_content
            
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
                
            print(f"Success for {lang_code}.")
        except Exception as e:
            print(f"Error {lang_code}: {e}")
    else:
        print(f"Warning: {lang_code}.json not found.")
