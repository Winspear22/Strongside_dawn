import json
import os

# Define translations for each language
translations = {
    "de": {
        "contact": {
            "title": "Kontakt",
            "back": "Zurück"
        },
        "cgv": {
            "title": "Allgemeine Verkaufsbedingungen",
            "back": "Zurück",
            "lastUpdate": "AGB aktualisiert am 16.12.2025",
            "sections": {
                "preliminary": {
                    "title": "Präambel",
                    "text": "Diese allgemeinen Verkaufsbedingungen werden einerseits von STRONGSIDE Technologies, betrieben von Adam Aloui, im Folgenden \"der Verkäufer\" genannt, Betreiber der Website https://www.strongside.tech/, und andererseits von jeder natürlichen oder juristischen Person abgeschlossen, die einen Kauf über die Website https://www.strongside.tech/ tätigen möchte, im Folgenden \"der Käufer\" genannt."
                },
                "object": {
                    "title": "Artikel 1. Vertragsgegenstand",
                    "text1": "Zweck dieser allgemeinen Verkaufsbedingungen ist es, die vertraglichen Beziehungen zwischen STRONGSIDE Technologies und dem Käufer sowie die Bedingungen zu definieren, die für jeden Kauf gelten, der über die Website https://www.strongside.tech/ getätigt wird.",
                    "text2": "Der Kauf eines Produkts über diese Website setzt die vorbehaltlose Annahme dieser allgemeinen Verkaufsbedingungen durch den Käufer voraus, der bestätigt, diese vor seiner Bestellung gelesen zu haben.",
                    "text3": "Vor jeder Transaktion erklärt der Käufer, dass er die volle Rechtsfähigkeit besitzt, um sich an diese allgemeinen Verkaufsbedingungen zu binden.",
                    "text4": "STRONGSIDE Technologies behält sich das Recht vor, diese allgemeinen Verkaufsbedingungen jederzeit zu ändern, um neuen Vorschriften zu entsprechen oder die Nutzung seiner Website zu verbessern. Die geltenden Bedingungen sind die zum Zeitpunkt der Bestellung gültigen."
                },
                "products": {
                    "title": "Artikel 2. Produkte",
                    "text1": "Die angebotenen Produkte sind diejenigen, die auf der Website https://www.strongside.tech/ aufgeführt sind, solange der Vorrat reicht. STRONGSIDE Technologies behält sich das Recht vor, das Produktsortiment jederzeit zu ändern.",
                    "text2": "Jedes Produkt wird auf der Website mit einer Beschreibung seiner wichtigsten technischen Merkmale präsentiert. Die Fotos sind so genau wie möglich, binden den Verkäufer jedoch nicht vertraglich."
                },
                "prices": {
                    "title": "Artikel 3. Preise",
                    "text1": "Die auf den Produktseiten angegebenen Preise verstehen sich in Euro (€) inklusive aller Steuern (MwSt.), die am Tag der Bestellung gelten.",
                    "text2": "STRONGSIDE Technologies behält sich das Recht vor, seine Preise jederzeit zu ändern, wobei der zum Zeitpunkt der Bestellung angezeigte Preis der einzige für den Käufer geltende Preis ist.",
                    "text3": "Die angegebenen Preise enthalten keine Versandkosten, die separat basierend auf dem Gesamtbestellwert und dem Bestimmungsort berechnet werden."
                },
                "order": {
                    "title": "Artikel 4. Bestellung und Zahlung",
                    "text1": "Vor jeder Bestellung muss der Käufer ein Konto auf der Website https://www.strongside.tech/ erstellen.",
                    "paymentMethods": "Akzeptierte Zahlungsmethoden sind:",
                    "method_card": "Kreditkarte",
                    "method_paypal": "PayPal",
                    "method_transfer": "Banküberweisung",
                    "method_other": "Jede andere Zahlungsmethode, die zum Zeitpunkt der Bestellung auf der Website angeboten wird",
                    "text2": "Die Bestätigung der Bestellung bedeutet die vollständige und uneingeschränkte Annahme dieser allgemeinen Verkaufsbedingungen.",
                    "text3": "Eine Auftragsbestätigung wird dem Käufer per E-Mail zugesandt."
                },
                "ownership": {
                    "title": "Artikel 5. Eigentumsvorbehalt",
                    "text": "STRONGSIDE Technologies behält sich das volle Eigentum an den verkauften Produkten bis zur vollständigen Zahlung des Preises, einschließlich Kosten und Steuern, vor."
                },
                "returns": {
                    "title": "Artikel 6. Widerrufsrecht und Rücksendungen",
                    "text1": "Gemäß den geltenden Gesetzen hat der Käufer vierzehn (14) Tage ab Erhalt seiner Bestellung Zeit, um sein Widerrufsrecht auszuüben.",
                    "highlight": "Rücksendungen werden innerhalb von 14 Tagen akzeptiert.",
                    "text2": "Produkte müssen im Originalzustand, unbenutzt und in der Originalverpackung zurückgesendet werden.",
                    "text3": "Die Rücksendekosten trägt der Käufer.",
                    "text4": "Die Rückerstattung erfolgt nach Eingang und Überprüfung der zurückgesandten Produkte."
                },
                "delivery": {
                    "title": "Artikel 7. Lieferung",
                    "text1": "Lieferungen erfolgen an die zum Zeitpunkt der Bestellung angegebene Adresse.",
                    "text2": "Lieferzeiten sind Richtwerte. Bei einer Verzögerung von mehr als dreißig (30) Tagen kann der Käufer die Stornierung der Bestellung und eine Rückerstattung verlangen.",
                    "text3": "Das Transportrisiko geht mit Übergabe des Pakets an den Spediteur auf den Käufer über."
                },
                "warranty": {
                    "title": "Artikel 8. Gewährleistung",
                    "text1": "Alle Produkte unterliegen den gesetzlichen Garantien für Konformität und versteckte Mängel gemäß den geltenden gesetzlichen Bestimmungen.",
                    "text2": "Jede Reklamation, jeder Umtausch oder Rückerstattungsantrag muss per E-Mail oder Post innerhalb von dreißig (30) Tagen nach Lieferung erfolgen."
                },
                "liability": {
                    "title": "Artikel 9. Haftung",
                    "text": "STRONGSIDE Technologies kann nicht für Schäden haftbar gemacht werden, die aus der Nutzung des Internets resultieren, wie z.B. Datenverlust, Eindringen, Viren oder Dienstunterbrechungen."
                },
                "ip": {
                    "title": "Artikel 10. Geistiges Eigentum",
                    "text1": "Alle Elemente der Website https://www.strongside.tech/ sind und bleiben das exklusive geistige Eigentum von STRONGSIDE Technologies.",
                    "text2": "Jede Reproduktion, Verwertung oder Nutzung, auch teilweise, ohne vorherige Genehmigung ist strengstens untersagt."
                },
                "data": {
                    "title": "Artikel 11. Personenbezogene Daten",
                    "text1": "STRONGSIDE Technologies verpflichtet sich, die Vertraulichkeit der vom Käufer angegebenen persönlichen Informationen zu wahren.",
                    "text2": "Gemäß den Datenschutzgesetzen und der DSGVO hat der Käufer das Recht auf Zugang, Berichtigung und Löschung seiner personenbezogenen Daten."
                },
                "disputes": {
                    "title": "Artikel 12. Streitbeilegung",
                    "text1": "Diese allgemeinen Verkaufsbedingungen unterliegen französischem Recht.",
                    "text2": "Im Streitfall wird vor jeder rechtlichen Maßnahme eine gütliche Lösung angestrebt. Andernfalls sind die Gerichte am Wohnsitz des Beklagten oder am Ort der Lieferung zuständig."
                },
                "entirety": {
                    "title": "Artikel 13. Gesamtheit",
                    "text": "Sollte eine Klausel dieser allgemeinen Verkaufsbedingungen für nichtig erklärt werden, behalten die anderen Klauseln ihre volle Gültigkeit."
                },
                "duration": {
                    "title": "Artikel 14. Dauer",
                    "text": "Diese Bedingungen gelten für die gesamte Dauer der von STRONGSIDE Technologies angebotenen Online-Dienste."
                },
                "proof": {
                    "title": "Artikel 15. Beweis",
                    "text": "Die in den Computersystemen von STRONGSIDE Technologies gespeicherten computergestützten Aufzeichnungen gelten als Beweis für die Kommunikation, Bestellungen und Zahlungen zwischen den Parteien."
                }
            }
        },
        "legal": {
            "title": "Impressum",
            "back": "Zurück",
            "lastUpdate": "Rechtliche Hinweise aktualisiert am 15.12.2025",
            "sections": {
                "identification": {
                    "title": "Identifikation und Veröffentlichung",
                    "editor": "Herausgeber",
                    "editorText": "Diese Website wird herausgegeben von ADAM ALOUI – STRONGSIDE Technologies.",
                    "director": "Veröffentlichungsdirektor: Adam Aloui",
                    "host": "Host",
                    "hostText": "Diese Website wird gehostet von Vercel Inc., 340 S Lemon Ave #4133, Walnut, CA 91789, USA."
                },
                "ip": {
                    "title": "Geistiges Eigentum",
                    "protection": "Alle grafischen Elemente, die Struktur und generell der Inhalt der Website von STRONGSIDE Technologies sind urheberrechtlich, markenrechtlich und geschmacksmusterrechtlich geschützt.",
                    "privateUse": "Jeder, der Inhalte oder Informationen von der Website sammelt oder herunterlädt, hat nur ein privates, persönliches und nicht übertragbares Nutzungsrecht.",
                    "reproduction": "Die Reproduktion einer Seite der Website in einem Kontext außerhalb von STRONGSIDE oder das Einfügen einer Seite von STRONGSIDE in die Seite einer anderen Website ist untersagt.",
                    "sanctions": "Ebenso ist jede Reproduktion oder Darstellung der Website ganz oder teilweise ohne schriftliche Zustimmung von STRONGSIDE untersagt und würde eine Verletzung darstellen, die nach den geltenden Gesetzen zum geistigen Eigentum strafbar ist.",
                    "paperReproduction": "Texte, Grafiken, Zeichnungen, Logos und Fotos, die von STRONGSIDE veröffentlicht werden, können auf Papier oder elektronischen Medien reproduziert werden, sofern der Name und die Adresse der Website angegeben werden und keine kommerzielle Nutzung erfolgt.",
                    "infringement": "Die Nichteinhaltung der oben genannten Bestimmungen kann eine Verletzung darstellen, die eine zivil- oder strafrechtliche Haftung des Urhebers nach sich zieht.",
                    "hyperlink": "Das Erstellen eines Hyperlinks zur Website www.strongside.tech darf nur mit Genehmigung von STRONGSIDE erfolgen, vorausgesetzt, dass keine Verwirrung hinsichtlich der Identität der Website oder der Herkunft der Informationen bei den Nutzern entstehen kann."
                },
                "data": {
                    "title": "Datenschutz & Cookies",
                    "intro": "Wir verwenden Tracking-Technologien, um Ihr Erlebnis zu verbessern und zu analysieren, wie unsere Website genutzt wird.",
                    "ga4Title": "Google Analytics 4",
                    "ga4Text": "Wir verwenden Google Analytics 4, um zu verstehen, wie Besucher mit unserer Website interagieren. Diese Daten sind anonymisiert und helfen uns, Ihr Surferlebnis zu optimieren. Es werden keine persönlich identifizierbaren Informationen gesammelt.",
                    "shopifyTitle": "Shopify",
                    "shopifyText": "Zahlungstransaktionen werden sicher von Shopify Payments verwaltet. Während des Bestellvorgangs kann Shopify Informationen sammeln, die zur Bearbeitung Ihrer Bestellung erforderlich sind (Name, Adresse, E-Mail, Zahlungsinformationen) gemäß deren Datenschutzrichtlinie.",
                    "vercelTitle": "Vercel Analytics",
                    "vercelText": "Unser Hosting-Anbieter Vercel sammelt anonymisierte Leistungsdaten, um die Geschwindigkeit der Website zu optimieren.",
                    "consent": "Durch die weitere Nutzung dieser Website stimmen Sie der Verwendung dieser Tracking-Technologien zu."
                }
            }
        }
    },
    "es": {
        "contact": {
            "title": "Contacto",
            "back": "Atrás"
        },
        "cgv": {
            "title": "Condiciones Generales de Venta",
            "back": "Atrás",
            "lastUpdate": "CGV actualizadas el 16/12/2025",
            "sections": {
                "preliminary": {
                    "title": "Artículo Preliminar",
                    "text": "Estas condiciones generales de venta se celebran, por una parte, por STRONGSIDE Technologies, operada por Adam Aloui, en adelante denominado 'el Vendedor', que opera el sitio web https://www.strongside.tech/, y, por otra parte, por cualquier persona física o jurídica que desee realizar una compra a través del sitio web https://www.strongside.tech/, en adelante denominada 'el Comprador'."
                },
                "object": {
                    "title": "Artículo 1. Objeto",
                    "text1": "El objeto de estas condiciones generales de venta es definir la relación contractual entre STRONGSIDE Technologies y el Comprador, así como las condiciones aplicables a cualquier compra realizada a través del sitio web https://www.strongside.tech/.",
                    "text2": "La compra de un producto a través de este sitio implica la aceptación sin reservas por parte del Comprador de estas condiciones generales de venta, que reconoce haber leído antes de realizar su pedido.",
                    "text3": "Antes de cualquier transacción, el Comprador declara tener plena capacidad legal para comprometerse con estas condiciones generales de venta.",
                    "text4": "STRONGSIDE Technologies se reserva el derecho de modificar estas condiciones generales de venta en cualquier momento para cumplir con nuevas regulaciones o mejorar el uso de su sitio. Las condiciones aplicables serán las vigentes en la fecha del pedido."
                },
                "products": {
                    "title": "Artículo 2. Productos",
                    "text1": "Los productos ofrecidos son los que figuran en el sitio web https://www.strongside.tech/, sujetos a disponibilidad. STRONGSIDE Technologies se reserva el derecho de modificar la gama de productos en cualquier momento.",
                    "text2": "Cada producto se presenta en el sitio con una descripción de sus principales características técnicas. Las fotografías son lo más precisas posible pero no vinculan al Vendedor."
                },
                "prices": {
                    "title": "Artículo 3. Precios",
                    "text1": "Los precios mostrados en las páginas de productos están en euros (€), incluidos todos los impuestos (IVA) aplicables en la fecha del pedido.",
                    "text2": "STRONGSIDE Technologies se reserva el derecho de modificar sus precios en cualquier momento, entendiéndose que el precio mostrado en el momento del pedido será el único aplicable al Comprador.",
                    "text3": "Los precios mostrados no incluyen los gastos de envío, que se cobran por separado según el importe total del pedido y el destino."
                },
                "order": {
                    "title": "Artículo 4. Pedido y Pago",
                    "text1": "Antes de cualquier pedido, el Comprador debe crear una cuenta en el sitio web https://www.strongside.tech/.",
                    "paymentMethods": "Los métodos de pago aceptados son:",
                    "method_card": "Tarjeta de crédito",
                    "method_paypal": "PayPal",
                    "method_transfer": "Transferencia bancaria",
                    "method_other": "Cualquier otro método de pago ofrecido en el sitio en el momento del pedido",
                    "text2": "La validación del pedido implica la aceptación plena y completa de estas condiciones generales de venta.",
                    "text3": "Se enviará una confirmación de pedido por correo electrónico al Comprador."
                },
                "ownership": {
                    "title": "Artículo 5. Reserva de Dominio",
                    "text": "STRONGSIDE Technologies conserva la plena propiedad de los productos vendidos hasta el pago completo del precio, incluidos gastos e impuestos."
                },
                "returns": {
                    "title": "Artículo 6. Derecho de Desistimiento y Devoluciones",
                    "text1": "De acuerdo con la legislación aplicable, el Comprador dispone de catorce (14) días a partir de la recepción de su pedido para ejercer su derecho de desistimiento.",
                    "highlight": "Se aceptan devoluciones dentro de los 14 días.",
                    "text2": "Los productos deben devolverse en su estado original, sin usar y en su embalaje original.",
                    "text3": "Los gastos de devolución corren a cargo del Comprador.",
                    "text4": "El reembolso se realizará tras la recepción y verificación de los productos devueltos."
                },
                "delivery": {
                    "title": "Artículo 7. Entrega",
                    "text1": "Las entregas se realizan a la dirección indicada en el momento del pedido.",
                    "text2": "Los plazos de entrega son indicativos. En caso de retraso superior a treinta (30) días, el Comprador podrá solicitar la cancelación del pedido y el reembolso.",
                    "text3": "El riesgo del transporte se transfiere al Comprador en el momento de la entrega del paquete al transportista."
                },
                "warranty": {
                    "title": "Artículo 8. Garantía",
                    "text1": "Todos los productos se benefician de las garantías legales de conformidad y vicios ocultos según lo dispuesto por la legislación aplicable.",
                    "text2": "Cualquier reclamación, solicitud de cambio o reembolso debe realizarse por correo electrónico o postal dentro de los treinta (30) días siguientes a la entrega."
                },
                "liability": {
                    "title": "Artículo 9. Responsabilidad",
                    "text": "STRONGSIDE Technologies no se hace responsable de los daños resultantes del uso de Internet, como pérdida de datos, intrusión, virus o interrupción del servicio."
                },
                "ip": {
                    "title": "Artículo 10. Propiedad Intelectual",
                    "text1": "Todos los elementos del sitio web https://www.strongside.tech/ son y seguirán siendo propiedad intelectual exclusiva de STRONGSIDE Technologies.",
                    "text2": "Cualquier reproducción, explotación o uso, incluso parcial, sin autorización previa está estrictamente prohibido."
                },
                "data": {
                    "title": "Artículo 11. Datos Personales",
                    "text1": "STRONGSIDE Technologies se compromete a preservar la confidencialidad de la información personal proporcionada por el Comprador.",
                    "text2": "De acuerdo con las leyes de protección de datos y el RGPD, el Comprador tiene derecho a acceder, rectificar y eliminar sus datos personales."
                },
                "disputes": {
                    "title": "Artículo 12. Resolución de Disputas",
                    "text1": "Estas condiciones generales de venta se rigen por la ley francesa.",
                    "text2": "En caso de disputa, se buscará una solución amistosa antes de cualquier acción legal. En su defecto, los tribunales competentes serán los del domicilio del demandado o del lugar de entrega."
                },
                "entirety": {
                    "title": "Artículo 13. Integridad",
                    "text": "Si alguna cláusula de estas condiciones generales de venta se declara nula, las demás cláusulas conservarán su plena validez."
                },
                "duration": {
                    "title": "Artículo 14. Duración",
                    "text": "Estas condiciones se aplican durante toda la duración de los servicios en línea ofrecidos por STRONGSIDE Technologies."
                },
                "proof": {
                    "title": "Artículo 15. Prueba",
                    "text": "Los registros informatizados conservados en los sistemas informáticos de STRONGSIDE Technologies constituirán prueba de las comunicaciones, pedidos y pagos entre las partes."
                }
            }
        },
        "legal": {
            "title": "Aviso Legal",
            "back": "Atrás",
            "lastUpdate": "Aviso legal actualizado el 15/12/2025",
            "sections": {
                "identification": {
                    "title": "Identificación y Publicación",
                    "editor": "Editor",
                    "editorText": "Este sitio es publicado por ADAM ALOUI – STRONGSIDE Technologies.",
                    "director": "Director de Publicación: Adam Aloui",
                    "host": "Host",
                    "hostText": "Este sitio está alojado por Vercel Inc., 340 S Lemon Ave #4133, Walnut, CA 91789, EE. UU."
                },
                "ip": {
                    "title": "Propiedad Intelectual",
                    "protection": "Todos los elementos gráficos, la estructura y, en general, el contenido del sitio de STRONGSIDE Technologies están protegidos por derechos de autor, derecho de marcas y derechos de diseño.",
                    "privateUse": "Cualquier persona que recopile o descargue contenido o información del sitio solo tiene un derecho de uso privado, personal e intransferible.",
                    "reproduction": "La reproducción de una página del sitio en un contexto externo a STRONGSIDE o la inserción de una página perteneciente a STRONGSIDE en la página de otro sitio está prohibida.",
                    "sanctions": "Del mismo modo, cualquier reproducción o representación del sitio total o parcialmente está prohibida sin el consentimiento por escrito de STRONGSIDE y constituiría una infracción sancionable según las leyes de propiedad intelectual aplicables.",
                    "paperReproduction": "Los textos, gráficos, dibujos, logotipos y fotos publicados por STRONGSIDE pueden reproducirse en papel o medios electrónicos, siempre que se cite el nombre y la dirección del sitio y no se haga uso comercial.",
                    "infringement": "El incumplimiento de las disposiciones anteriores puede constituir una infracción que implique la responsabilidad civil o penal del autor.",
                    "hyperlink": "La creación de un enlace de hipertexto al sitio www.strongside.tech solo puede hacerse con la autorización de STRONGSIDE, y siempre que no pueda existir confusión en la mente de los usuarios con respecto a la identidad del sitio o el origen de la información."
                },
                "data": {
                    "title": "Protección de Datos y Cookies",
                    "intro": "Utilizamos tecnologías de seguimiento para mejorar su experiencia y analizar cómo se utiliza nuestro sitio.",
                    "ga4Title": "Google Analytics 4",
                    "ga4Text": "Utilizamos Google Analytics 4 para entender cómo los visitantes interactúan con nuestro sitio. Estos datos son anónimos y nos ayudan a optimizar su experiencia de navegación. No se recopila información de identificación personal.",
                    "shopifyTitle": "Shopify",
                    "shopifyText": "Las transacciones de pago son gestionadas de forma segura por Shopify Payments. Durante el proceso de pago, Shopify puede recopilar información necesaria para procesar su pedido (nombre, dirección, correo electrónico, información de pago) de acuerdo con su política de privacidad.",
                    "vercelTitle": "Vercel Analytics",
                    "vercelText": "Nuestro proveedor de alojamiento Vercel recopila datos de rendimiento anónimos para optimizar la velocidad del sitio.",
                    "consent": "Al continuar utilizando este sitio, usted acepta el uso de estas tecnologías de seguimiento."
                }
            }
        }
    },
    "it": {
        "contact": {
            "title": "Contattaci",
            "back": "Indietro"
        },
        "cgv": {
            "title": "Condizioni Generali di Vendita",
            "back": "Indietro",
            "lastUpdate": "CGV aggiornate il 16/12/2025",
            "sections": {
                "preliminary": {
                    "title": "Articolo Preliminare",
                    "text": "Le presenti condizioni generali di vendita sono stipulate, da una parte, da STRONGSIDE Technologies, gestita da Adam Aloui, di seguito denominata 'il Venditore', che gestisce il sito web https://www.strongside.tech/, e, dall'altra parte, da qualsiasi persona fisica o giuridica che desideri effettuare un acquisto tramite il sito web https://www.strongside.tech/, di seguito denominata 'l'Acquirente'."
                },
                "object": {
                    "title": "Articolo 1. Oggetto",
                    "text1": "Oggetto delle presenti condizioni generali di vendita è definire il rapporto contrattuale tra STRONGSIDE Technologies e l'Acquirente, nonché le condizioni applicabili a qualsiasi acquisto effettuato tramite il sito web https://www.strongside.tech/.",
                    "text2": "L'acquisto di un prodotto tramite questo sito implica l'accettazione senza riserve da parte dell'Acquirente delle presenti condizioni generali di vendita, che riconosce di aver letto prima di effettuare l'ordine.",
                    "text3": "Prima di qualsiasi transazione, l'Acquirente dichiara di avere la piena capacità giuridica di impegnarsi con le presenti condizioni generali di vendita.",
                    "text4": "STRONGSIDE Technologies si riserva il diritto di modificare le presenti condizioni generali di vendita in qualsiasi momento per conformarsi a nuove normative o migliorare l'uso del proprio sito. Le condizioni applicabili saranno quelle in vigore alla data dell'ordine."
                },
                "products": {
                    "title": "Articolo 2. Prodotti",
                    "text1": "I prodotti offerti sono quelli elencati sul sito web https://www.strongside.tech/, in base alla disponibilità. STRONGSIDE Technologies si riserva il diritto di modificare la gamma di prodotti in qualsiasi momento.",
                    "text2": "Ogni prodotto è presentato sul sito con una descrizione delle sue principali caratteristiche tecniche. Le fotografie sono il più accurate possibile ma non vincolano il Venditore."
                },
                "prices": {
                    "title": "Articolo 3. Prezzi",
                    "text1": "I prezzi indicati nelle pagine dei prodotti sono in euro (€), comprensivi di tutte le tasse (IVA) applicabili alla data dell'ordine.",
                    "text2": "STRONGSIDE Technologies si riserva il diritto di modificare i propri prezzi in qualsiasi momento, restando inteso che il prezzo visualizzato al momento dell'ordine sarà l'unico applicabile all'Acquirente.",
                    "text3": "I prezzi indicati non includono le spese di spedizione, che vengono addebitate separatamente in base all'importo totale dell'ordine e alla destinazione."
                },
                "order": {
                    "title": "Articolo 4. Ordine e Pagamento",
                    "text1": "Prima di qualsiasi ordine, l'Acquirente deve creare un account sul sito web https://www.strongside.tech/.",
                    "paymentMethods": "I metodi di pagamento accettati sono:",
                    "method_card": "Carta di credito",
                    "method_paypal": "PayPal",
                    "method_transfer": "Bonifico bancario",
                    "method_other": "Qualsiasi altro metodo di pagamento offerto sul sito al momento dell'ordine",
                    "text2": "La convalida dell'ordine implica l'accettazione piena e completa delle presenti condizioni generali di vendita.",
                    "text3": "Una conferma d'ordine verrà inviata via email all'Acquirente."
                },
                "ownership": {
                    "title": "Articolo 5. Riserva di Proprietà",
                    "text": "STRONGSIDE Technologies conserva la piena proprietà dei prodotti venduti fino al completo pagamento del prezzo, incluse tasse e spese."
                },
                "returns": {
                    "title": "Articolo 6. Diritto di Recesso e Resi",
                    "text1": "In conformità con la legislazione applicabile, l'Acquirente ha quattordici (14) giorni dal ricevimento dell'ordine per esercitare il proprio diritto di recesso.",
                    "highlight": "I resi sono accettati entro 14 giorni.",
                    "text2": "I prodotti devono essere restituiti nelle loro condizioni originali, inutilizzati e nella confezione originale.",
                    "text3": "Le spese di restituzione rimangono a carico dell'Acquirente.",
                    "text4": "Il rimborso verrà effettuato dopo il ricevimento e la verifica dei prodotti restituiti."
                },
                "delivery": {
                    "title": "Articolo 7. Consegna",
                    "text1": "Le consegne vengono effettuate all'indirizzo indicato al momento dell'ordine.",
                    "text2": "I tempi di consegna sono indicativi. In caso di ritardo superiore a trenta (30) giorni, l'Acquirente può richiedere l'annullamento dell'ordine e il rimborso.",
                    "text3": "I rischi del trasporto vengono trasferiti all'Acquirente al momento della consegna del pacco al corriere."
                },
                "warranty": {
                    "title": "Articolo 8. Garanzia",
                    "text1": "Tutti i prodotti beneficiano delle garanzie legali di conformità e vizi occulti come previsto dagli articoli del Codice Civile.",
                    "text2": "Qualsiasi reclamo, richiesta di cambio o rimborso deve essere effettuata via email o posta entro trenta (30) giorni dalla consegna."
                },
                "liability": {
                    "title": "Articolo 9. Responsabilità",
                    "text": "STRONGSIDE Technologies non può essere ritenuta responsabile per danni derivanti dall'uso di Internet, come perdita di dati, intrusioni, virus o interruzioni del servizio."
                },
                "ip": {
                    "title": "Articolo 10. Proprietà Intellettuale",
                    "text1": "Tutti gli elementi del sito web https://www.strongside.tech/ sono e rimangono proprietà intellettuale esclusiva di STRONGSIDE Technologies.",
                    "text2": "Qualsiasi riproduzione, sfruttamento o utilizzo, anche parziale, senza previa autorizzazione è severamente vietato."
                },
                "data": {
                    "title": "Articolo 11. Dati Personali",
                    "text1": "STRONGSIDE Technologies si impegna a preservare la riservatezza delle informazioni personali fornite dall'Acquirente.",
                    "text2": "In conformità con la legge sulla protezione dei dati e il GDPR, l'Acquirente ha il diritto di accedere, rettificare e cancellare i propri dati personali."
                },
                "disputes": {
                    "title": "Articolo 12. Risoluzione delle Controversie",
                    "text1": "Le presenti condizioni generali di vendita sono regolate dalla legge francese.",
                    "text2": "In caso di controversia, verrà cercata una soluzione amichevole prima di qualsiasi azione legale. In mancanza, i tribunali competenti saranno quelli del domicilio del convenuto o del luogo di consegna."
                },
                "entirety": {
                    "title": "Articolo 13. Interezza",
                    "text": "Se una qualsiasi clausola delle presenti condizioni generali di vendita è dichiarata nulla, le altre clausole manterranno la loro piena validità."
                },
                "duration": {
                    "title": "Articolo 14. Durata",
                    "text": "Queste condizioni si applicano per l'intera durata dei servizi online offerti da STRONGSIDE Technologies."
                },
                "proof": {
                    "title": "Articolo 15. Prova",
                    "text": "Le registrazioni computerizzate conservate nei sistemi informatici di STRONGSIDE Technologies costituiranno prova delle comunicazioni, degli ordini e dei pagamenti tra le parti."
                }
            }
        },
        "legal": {
            "title": "Note Legali",
            "back": "Indietro",
            "lastUpdate": "Note legali aggiornate il 15/12/2025",
            "sections": {
                "identification": {
                    "title": "Identificazione e Pubblicazione",
                    "editor": "Editore",
                    "editorText": "Questo sito è pubblicato da ADAM ALOUI – STRONGSIDE Technologies.",
                    "director": "Direttore della pubblicazione: Adam Aloui",
                    "host": "Provider",
                    "hostText": "Questo sito è ospitato da Vercel Inc., 340 S Lemon Ave #4133, Walnut, CA 91789, USA."
                },
                "ip": {
                    "title": "Proprietà Intellettuale",
                    "protection": "Tutti gli elementi grafici, la struttura e, più in generale, il contenuto del sito STRONGSIDE Technologies sono protetti da diritto d'autore, diritto dei marchi e diritti di design.",
                    "privateUse": "Chiunque raccolga o scarichi contenuti o informazioni dal sito ha solo un diritto di utilizzo privato, personale e non trasferibile.",
                    "reproduction": "La riproduzione di una pagina del sito in un contesto esterno a STRONGSIDE o l'inserimento di una pagina appartenente a STRONGSIDE nella pagina di un altro sito è vietata.",
                    "sanctions": "Allo stesso modo, qualsiasi riproduzione o rappresentazione del sito in tutto o in parte è vietata senza il consenso scritto di STRONGSIDE e costituirebbe una violazione punibile secondo le leggi sulla proprietà intellettuale vigenti.",
                    "paperReproduction": "Testi, grafiche, disegni, loghi e foto pubblicati da STRONGSIDE possono essere riprodotti su carta o supporti elettronici, a condizione che vengano citati il nome e l'indirizzo del sito e non ne venga fatto uso commerciale.",
                    "infringement": "Il mancato rispetto delle disposizioni di cui sopra può costituire una violazione che comporta la responsabilità civile o penale dell'autore.",
                    "hyperlink": "La creazione di un collegamento ipertestuale al sito www.strongside.tech può avvenire solo con l'autorizzazione di STRONGSIDE, e a condizione che non vi sia confusione nella mente degli utenti riguardo all'identità del sito o all'origine delle informazioni."
                },
                "data": {
                    "title": "Protezione dei Dati e Cookie",
                    "intro": "Utilizziamo tecnologie di tracciamento per migliorare la tua esperienza e analizzare come viene utilizzato il nostro sito.",
                    "ga4Title": "Google Analytics 4",
                    "ga4Text": "Utilizziamo Google Analytics 4 per capire come i visitatori interagiscono con il nostro sito. Questi dati sono anonimizzati e ci aiutano a ottimizzare la tua esperienza di navigazione. Non vengono raccolte informazioni personali identificabili.",
                    "shopifyTitle": "Shopify",
                    "shopifyText": "Le transazioni di pagamento sono gestite in modo sicuro da Shopify Payments. Durante il processo di checkout, Shopify può raccogliere informazioni necessarie per elaborare il tuo ordine (nome, indirizzo, email, informazioni di pagamento) in conformità con la loro politica sulla privacy.",
                    "vercelTitle": "Vercel Analytics",
                    "vercelText": "Il nostro provider di hosting Vercel raccoglie dati sulle prestazioni anonimizzati per ottimizzare la velocità del sito.",
                    "consent": "Continuando a utilizzare questo sito, acconsenti all'uso di queste tecnologie di tracciamento."
                }
            }
        }
    },
    "nl": {
        "contact": {
            "title": "Contact",
            "back": "Terug"
        },
        "cgv": {
            "title": "Algemene Verkoopvoorwaarden",
            "back": "Terug",
            "lastUpdate": "AV geüpdatet op 16/12/2025",
            "sections": {
                "preliminary": {
                    "title": "Inleidend Artikel",
                    "text": "Deze algemene verkoopvoorwaarden worden enerzijds aangegaan door STRONGSIDE Technologies, beheerd door Adam Aloui, hierna te noemen 'de Verkoper', exploitant van de website https://www.strongside.tech/, en anderzijds door elke natuurlijke of rechtspersoon die een aankoop wenst te doen via de website https://www.strongside.tech/, hierna te noemen 'de Koper'."
                },
                "object": {
                    "title": "Artikel 1. Doel",
                    "text1": "Het doel van deze algemene verkoopvoorwaarden is om de contractuele relatie tussen STRONGSIDE Technologies en de Koper vast te leggen, evenals de voorwaarden die van toepassing zijn op elke aankoop via de website https://www.strongside.tech/.",
                    "text2": "De aankoop van een product via deze site impliceert de onvoorwaardelijke aanvaarding door de Koper van deze algemene verkoopvoorwaarden, die hij erkent te hebben gelezen voorafgaand aan zijn bestelling.",
                    "text3": "Voor elke transactie verklaart de Koper dat hij de volledige wettelijke bevoegdheid heeft om zich te binden aan deze algemene verkoopvoorwaarden.",
                    "text4": "STRONGSIDE Technologies behoudt zich het recht voor om deze algemene verkoopvoorwaarden op elk moment te wijzigen om te voldoen aan nieuwe regelgeving of om het gebruik van zijn site te verbeteren. De toepasselijke voorwaarden zijn die welke van kracht zijn op de datum van de bestelling."
                },
                "products": {
                    "title": "Artikel 2. Producten",
                    "text1": "De aangeboden producten zijn die vermeld op de website https://www.strongside.tech/, zolang de voorraad strekt. STRONGSIDE Technologies behoudt zich het recht voor om het assortiment op elk moment te wijzigen.",
                    "text2": "Elk product wordt op de site gepresenteerd met een beschrijving van de belangrijkste technische kenmerken. De foto's zijn zo nauwkeurig mogelijk, maar binden de Verkoper niet."
                },
                "prices": {
                    "title": "Artikel 3. Prijzen",
                    "text1": "De prijzen getoond op productpagina's zijn in euro's (€), inclusief alle belastingen (BTW) die van toepassing zijn op de besteldatum.",
                    "text2": "STRONGSIDE Technologies behoudt zich het recht voor om zijn prijzen op elk moment te wijzigen, met dien verstande dat de prijs die wordt weergegeven op het moment van bestelling de enige is die van toepassing is op de Koper.",
                    "text3": "De getoonde prijzen zijn exclusief verzendkosten, die apart in rekening worden gebracht op basis van het totale bestelbedrag en de bestemming."
                },
                "order": {
                    "title": "Artikel 4. Bestelling en Betaling",
                    "text1": "Voor elke bestelling moet de Koper een account aanmaken op de website https://www.strongside.tech/.",
                    "paymentMethods": "Geaccepteerde betaalmethoden zijn:",
                    "method_card": "Creditcard",
                    "method_paypal": "PayPal",
                    "method_transfer": "Bankoverschrijving",
                    "method_other": "Elke andere betaalmethode die op de site wordt aangeboden op het moment van bestelling",
                    "text2": "De validatie van de bestelling impliceert de volledige en onvoorwaardelijke aanvaarding van deze algemene verkoopvoorwaarden.",
                    "text3": "Een orderbevestiging wordt per e-mail naar de Koper gestuurd."
                },
                "ownership": {
                    "title": "Artikel 5. Eigendomsvoorbehoud",
                    "text": "STRONGSIDE Technologies behoudt de volledige eigendom van de verkochte producten tot de volledige betaling van de prijs, inclusief kosten en belastingen."
                },
                "returns": {
                    "title": "Artikel 6. Herroepingsrecht en Retourzendingen",
                    "text1": "In overeenstemming met de toepasselijke wetgeving heeft de Koper veertien (14) dagen vanaf de ontvangst van zijn bestelling om zijn herroepingsrecht uit te oefenen.",
                    "highlight": "Retourzendingen worden binnen 14 dagen geaccepteerd.",
                    "text2": "Producten moeten in hun originele staat, ongebruikt en in hun originele verpakking worden geretourneerd.",
                    "text3": "Retourkosten blijven voor rekening van de Koper.",
                    "text4": "Terugbetaling zal plaatsvinden na ontvangst en verificatie van de geretourneerde producten."
                },
                "delivery": {
                    "title": "Artikel 7. Levering",
                    "text1": "Leveringen vinden plaats op het adres dat is opgegeven op het moment van bestelling.",
                    "text2": "Levertijden zijn indicatief. In geval van vertraging van meer dan dertig (30) dagen, kan de Koper annulering van de bestelling en terugbetaling verzoeken.",
                    "text3": "Het transportrisico gaat over op de Koper bij overdracht van het pakket aan de vervoerder."
                },
                "warranty": {
                    "title": "Artikel 8. Garantie",
                    "text1": "Alle producten vallen onder de wettelijke garanties van conformiteit en verborgen gebreken zoals bepaald door de artikelen van het Burgerlijk Wetboek.",
                    "text2": "Elke claim, verzoek om omruiling of terugbetaling moet per e-mail of post worden gedaan binnen dertig (30) dagen na levering."
                },
                "liability": {
                    "title": "Artikel 9. Aansprakelijkheid",
                    "text": "STRONGSIDE Technologies kan niet aansprakelijk worden gesteld voor schade die voortvloeit uit het gebruik van internet, zoals gegevensverlies, inbraak, virussen of serviceonderbreking."
                },
                "ip": {
                    "title": "Artikel 10. Intellectueel Eigendom",
                    "text1": "Alle elementen van de website https://www.strongside.tech/ zijn en blijven het exclusieve intellectuele eigendom van STRONGSIDE Technologies.",
                    "text2": "Elke reproductie, exploitatie of gebruik, zelfs gedeeltelijk, zonder voorafgaande toestemming is strikt verboden."
                },
                "data": {
                    "title": "Artikel 11. Persoonsgegevens",
                    "text1": "STRONGSIDE Technologies verbindt zich ertoe de vertrouwelijkheid van door de Koper verstrekte persoonlijke informatie te bewaren.",
                    "text2": "In overeenstemming met de wet op de gegevensbescherming en de AVG heeft de Koper het recht op toegang, correctie en verwijdering van zijn persoonsgegevens."
                },
                "disputes": {
                    "title": "Artikel 12. Geschillenbeslechting",
                    "text1": "Deze algemene verkoopvoorwaarden worden beheerst door Frans recht.",
                    "text2": "In geval van geschil zal een minnelijke oplossing worden gezocht voorafgaand aan elke gerechtelijke actie. Bij gebreke daarvan zijn de rechtbanken van de woonplaats van de verweerder of de plaats van levering bevoegd."
                },
                "entirety": {
                    "title": "Artikel 13. Volledigheid",
                    "text": "Indien een clausule van deze algemene verkoopvoorwaarden nietig wordt verklaard, behouden de overige clausules hun volledige geldigheid."
                },
                "duration": {
                    "title": "Artikel 14. Duur",
                    "text": "Deze voorwaarden zijn van toepassing gedurende de gehele duur van de online diensten aangeboden door STRONGSIDE Technologies."
                },
                "proof": {
                    "title": "Artikel 15. Bewijs",
                    "text": "De gecomputeriseerde registers die in de computersystemen van STRONGSIDE Technologies worden bewaard, vormen het bewijs van communicatie, bestellingen en betalingen tussen de partijen."
                }
            }
        },
        "legal": {
            "title": "Juridische Kennisgeving",
            "back": "Terug",
            "lastUpdate": "Juridische kennisgeving geüpdatet op 15/12/2025",
            "sections": {
                "identification": {
                    "title": "Identificatie en Publicatie",
                    "editor": "Uitgever",
                    "editorText": "Deze site wordt uitgegeven door ADAM ALOUI – STRONGSIDE Technologies.",
                    "director": "Publicatiedirecteur: Adam Aloui",
                    "host": "Host",
                    "hostText": "Deze site wordt gehost door Vercel Inc., 340 S Lemon Ave #4133, Walnut, CA 91789, VS."
                },
                "ip": {
                    "title": "Intellectueel Eigendom",
                    "protection": "Alle grafische elementen, de structuur en meer in het algemeen de inhoud van de site van STRONGSIDE Technologies zijn beschermd door auteursrecht, merkenrecht en modelrechten.",
                    "privateUse": "Iedereen die inhoud of informatie van de site verzamelt of downloadt, heeft slechts een privé, persoonlijk en niet-overdraagbaar gebruiksrecht.",
                    "reproduction": "Reproductie van een pagina van de site in een context buiten STRONGSIDE of invoeging van een pagina behorend tot STRONGSIDE in de pagina van een andere site is verboden.",
                    "sanctions": "Evenzo is elke reproductie of weergave van de site geheel of gedeeltelijk verboden zonder de schriftelijke toestemming van STRONGSIDE en zou dit een inbreuk vormen die strafbaar is volgens de toepasselijke wetten inzake intellectueel eigendom.",
                    "paperReproduction": "Teksten, grafieken, tekeningen, logo's en foto's gepubliceerd door STRONGSIDE kunnen worden gereproduceerd op papier of elektronische media, mits de naam en het adres van de site worden vermeld en er geen commercieel gebruik wordt gemaakt.",
                    "infringement": "Niet-naleving van bovenstaande bepalingen kan een inbreuk vormen die de civiele of strafrechtelijke aansprakelijkheid van de auteur met zich meebrengt.",
                    "hyperlink": "Het maken van een hyperlink naar de site www.strongside.tech kan alleen met toestemming van STRONGSIDE, en mits er geen verwarring kan bestaan bij gebruikers over de identiteit van de site of de oorsprong van informatie."
                },
                "data": {
                    "title": "Gegevensbescherming & Cookies",
                    "intro": "We gebruiken trackingtechnologieën om uw ervaring te verbeteren en te analyseren hoe onze site wordt gebruikt.",
                    "ga4Title": "Google Analytics 4",
                    "ga4Text": "We gebruiken Google Analytics 4 om te begrijpen hoe bezoekers onze site gebruiken. Deze gegevens worden geanonimiseerd en helpen ons uw browse-ervaring te optimaliseren. Er wordt geen persoonlijk identificeerbare informatie verzameld.",
                    "shopifyTitle": "Shopify",
                    "shopifyText": "Betalingstransacties worden veilig beheerd door Shopify Payments. Tijdens het afrekenproces kan Shopify informatie verzamelen die nodig is voor het verwerken van uw bestelling (naam, adres, e-mail, betalingsinformatie) in overeenstemming met hun privacybeleid.",
                    "vercelTitle": "Vercel Analytics",
                    "vercelText": "Onze hostingprovider Vercel verzamelt geanonimiseerde prestatiegegevens om de snelheid van de site te optimaliseren.",
                    "consent": "Door deze site te blijven gebruiken, stemt u in met het gebruik van deze trackingtechnologieën."
                }
            }
        }
    }
}

locales_dir = 'dawn/locales'

for lang_code, translation_content in translations.items():
    file_path = os.path.join(locales_dir, f"{lang_code}.json")
    
    if not os.path.exists(file_path):
        print(f"Warning: {file_path} does not exist, skipping.")
        continue
        
    print(f"Injecting translations into {file_path}...")
    
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
        print(f"Error processing {lang_code}: {e}")
