# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 87 (printed ٨٦).

The examples of the grounds preventing full declension (asbāb manʿ al-ṣarf)
and the ruling of the non-declinable noun (al-ism ghayr al-munṣarif).
"""

PAGE_NUMBER = 87
PRINTED_PAGE = "٨٦"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The base text (matn) ----------------
    {"type": "matn",
     "ar": "(وأحمر) مثال للوصف.",
     "en": "“(Wa-aḥmar)” — an example of the adjectival ground (waṣf)."},
    {"type": "matn",
     "ar": "(وطلحة) مثال للتأنيث.",
     "en": "“(Wa-Ṭalḥa)” — an example of feminization (taʾnīth)."},
    {"type": "matn",
     "ar": "(وزينب) مثال للمعرفة.",
     "en": "“(Wa-Zaynab)” — an example of definiteness (maʿrifa, i.e. a proper name)."},
    {"type": "matn",
     "ar": "وفي إيراد «زينب» مثالا للمعرفة بعد «طلحة» إشارة إلى قسمي التأنيث اللفظي والمعنوي[[١]].",
     "en": "In adducing “Zaynab” as an example of definiteness after “Ṭalḥa” there is an indication of the two kinds of feminization: the formal (lafẓī) and the semantic (maʿnawī)."},
    {"type": "matn",
     "ar": "(وإبراهيم) مثال للعجمة.",
     "en": "“(Wa-Ibrāhīm)” — an example of foreignness (ʿujma)."},
    {"type": "matn",
     "ar": "(ومساجد) مثال للجمع.",
     "en": "“(Wa-masājid)” — an example of the [ultimate-]plural pattern (jamʿ)."},
    {"type": "matn",
     "ar": "(ومعدي كرب) مثال للتركيب.",
     "en": "“(Wa-Maʿdī Karib)” — an example of compounding (tarkīb)."},
    {"type": "matn",
     "ar": "(وعمران) مثال للألف والنون.",
     "en": "“(Wa-ʿImrān)” — an example of the [adjunct] alif and nūn."},
    {"type": "matn",
     "ar": "(وأحمد) مثال لوزن الفعل.",
     "en": "“(Wa-Aḥmad)” — an example of the pattern of the verb (wazn al-fiʿl)."},
    {"type": "matn",
     "ar": "(وحكمه) أي: حكم غير المنصرف[[٢]]، والأثر المترتب[[٣]] عليه من حيث اشتماله على علتين[[٤]]، أو علة واحدة تقوم مقامهما: (أن لا كسر) فيه (ولا تنوين)[[٥]].",
     "en": "“(Wa-ḥukmuhu)” — that is: the ruling of the non-declinable noun (ghayr al-munṣarif), and the effect entailed upon it inasmuch as it comprises two causes, or a single cause standing in place of the two, is: “(an lā kasr)” — that there be no kasra in it — “(wa-lā tanwīn)” — nor tanwīn."},
    {"type": "matn",
     "ar": "وذلك لأن لكل علة فرعية[[٦]]، فإذا وقع في الاسم علتان[[٧]] حصل فيه فرعيتان، فيشبه الفعل[[٨]] من حيث إن له فرعيتين بالنسبة إلى الاسم:",
     "en": "That is because every cause [confers] a secondariness (farʿiyya); so when two causes occur in the noun, two secondarinesses arise in it, whereby it comes to resemble the verb, inasmuch as the verb has two secondarinesses relative to the noun:"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "يعني: أن التأنيث اللفظي معتبر وإن كان مع التذكير الحقيقي الذي لا يعتبر تأنيث الفعل معه، فلا يقال: جاءت طلحة، وكذا المعنوي الذي خفي فيه العلامة.",
     "en": "That is: formal feminization is taken into account [as a ground preventing declension] even when it co-occurs with real masculinity — with which the feminine [conjugation] of the verb is not applied, so one does not say “jāʾat Ṭalḥa” (Ṭalḥa [m.] came [f.]) — and likewise the semantic [feminization], in which the [feminine] marker is hidden."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "الظاهر أن الإضافة للاستغراق.",
     "en": "Apparently the genitive construction [in “ḥukmuhu”] denotes all-inclusiveness (istighrāq)."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "عطف تفسير للحكم، وإشارة إلى أن الحكم ههنا بمعنى الحكم المتعارف عند الأصوليين.",
     "en": "[The phrase “the effect entailed”] is an explicative apposition to “the ruling,” and an indication that “ruling” here bears the sense of “ruling” as conventionally understood among the legal theorists (uṣūliyyūn)."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "إنما قال ذلك؛ لأن الحكم يضاف إلى العلة حقيقة لا إلى ما فيه العلة. ورجع الضمير إلى وجود أحد الأمرين من العلتين، وما يقوم مقامهما صرف عن المنساق إلى الفهم.",
     "en": "He said this only because the ruling is attributed, in reality, to the cause itself, not to that in which the cause resides. And referring the pronoun back to the existence of one of the two matters — [namely] the two causes and what stands in their place — is a diversion from the natural drift [of the wording] (al-munsāq) toward [mere] comprehension."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "إنما ذكر الكسرة ههنا مع أن انتفاءها قد علم بقوله: غير المنصرف بالضمة والفتحة؛ لأنه أراد الجمع بين الحكمين، فإنه أقرب ضبطا.",
     "en": "He mentioned the kasra here even though its negation was already known from his statement “the non-declinable [is inflected] with ḍamma and fatḥa,” because he wished to combine the two rulings, for it is nearer to precise retention."},
    {"type": "pair",
     "ar": "ولا يخفى أن ذلك الحكم لم يظهر في المثنى وجمع المذكر السالم علمين للمؤنث، إلا إذا أعربا إعراب المفرد، كما ذهب إليه بعضهم.",
     "en": "And it is not hidden that this ruling does not manifest in the dual and the sound masculine plural when they are proper names for a feminine [referent], except when they are inflected with the inflection of the singular, as some have held."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "اعلم أن الفرعية لا تختص بفرعية الموقوف عليه، بل يشملها وغيرها كفرعية المرجوح للراجح، وأنها لا تنحصر فيما ذكر ككون الاسم مثنى إلى غير ذلك، لكن لم يعتبروها ولم يعلم وجهه.",
     "en": "Know that “secondariness” is not restricted to the secondariness of that which is depended upon (al-mawqūf ʿalayhi); rather it encompasses that and others, such as the secondariness of the outweighed relative to the outweighing; and [know] that it is not confined to what has been mentioned, such as the noun’s being a dual, and so on. But they did not take these into account, nor was the reason for it made known."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "لم يقنع بفرعية واحدة؛ لأن المشابهة بالفرعية غير ظاهرة، ولا قوية؛ إذ الفرعية ليست من خصائص الفعل الظاهرة، بل يحتاج في إثباتها إلى تكلف.",
     "en": "He was not content with a single secondariness, because the resemblance [to the verb] through secondariness is neither evident nor strong; for secondariness is not among the manifest properties of the verb, but rather requires artificial effort to establish."},
    {"type": "pair",
     "ar": "وكذا إثبات الفرعية في الأسماء بسبب هذه العلل خفي، ولم تكف واحدة إلا إذا قامت مقام اثنتين.",
     "en": "Likewise the establishing of secondariness in nouns by reason of these causes is subtle; and a single [cause] does not suffice unless it stands in the place of two."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "اعلم أن أصل الاسم الإعراب، وأصل الفعل العمل والبناء، فإذا شابه الاسم الفعل في تمام معناه، كما في أسماء الأفعال يبنى، ويعطى عمله،",
     "en": "Know that the primary state of the noun is [full] inflection (iʿrāb), while the primary state of the verb is governance (ʿamal) and indeclinability (bināʾ); so when a noun resembles the verb in the entirety of its meaning — as in the verbal nouns (asmāʾ al-afʿāl) — it is made indeclinable and is given the verb’s governing power;"},
    {"type": "pair",
     "ar": "وإذا شابهه في تركيب الحروف الأصلية، وفي جزء معناه كاسم",
     "en": "and when it resembles it in the composition of the radical letters, and in part of its meaning — as in the [active-participial] noun…"},
]
