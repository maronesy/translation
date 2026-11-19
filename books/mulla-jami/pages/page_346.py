# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 346 (printed ٣٤٥)."""

PAGE_NUMBER = 346
PRINTED_PAGE = "٣٤٥"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «… و«أبتع»، و«أبصع»)» from the foot of PDF p. 345.
    {"type": "matn",
     "ar": "بالصاد المهملة. وقيل: بالضاد المعجمة.",
     "en": "… with the undotted ṣād; it is also said: with the dotted ḍād."},
    {"type": "matn",
     "ar": "قيل: لا معنى لهذه الكلمات الثلاث في حال الإفراد مثل: «جسق بسن».",
     "en": "It is said that these three words have no meaning when standing alone, like “jasiq basin”."},
    {"type": "matn",
     "ar": "وقيل: «أكتع» مشتق من «حول كتيع» أي: تام، و«أبصع» بالصاد المهملة من «بصع العرق» أي: سال، وبالمعجمة من «بضع» أي: روي، و«أبتع» من «البتع»، وهو طول العنق مع شدة مغرزه،",
     "en": "It is also said that “aktaʿ” is derived from “ḥawlun katīʿun” (a full year), that is, complete; “abṣaʿ”, with the undotted ṣād, from “baṣaʿa al-ʿaraqu” (the sweat flowed), that is, it ran, and with the dotted [ḍād] from “baḍaʿa”, that is, he was quenched; and “abtaʿ” from “al-bataʿ”, which is length of neck together with firmness of its base."},
    {"type": "matn",
     "ar": "ويمكن استنباط مناسبات خفية[[١]] بين هذه المعاني ومعناها التأكيدي بالتأمل الصادق.",
     "en": "Hidden correspondences between these meanings and their corroborative meaning can be drawn out by careful reflection."},
    {"type": "matn",
     "ar": "(فالأولان) أي: «النفس والعين» (يعمان) أي: يقعان[[٢]] على الواحد والمثنى والمجموع والمذكر والمؤنث (باختلاف صيغتهما) إفرادا وتثنية وجمعا (و) اختلاف (ضميرهما) العائد إلى المتبوع المؤكد",
     "en": "(The first two), that is, “al-nafs” and “al-ʿayn”, (are general), that is, they apply to the singular, the dual, the plural, the masculine and the feminine, (by the variation of their form) as singular, dual and plural, (and) the variation of (their pronoun) referring to the corroborated word followed."},
    {"type": "matn",
     "ar": "(تقول: «نفسه») في المذكر الواحد («نفسها») في المؤنث الواحدة (و«أنفسهما») بإيراد صيغة الجمع في تثنية المذكر والمؤنث[[٣]]، وعن بعض العرب: «نفساهما وعيناهما»[[٤]]",
     "en": "(You say “nafsuhu”) for the masculine singular, (“nafsuhā”) for the feminine singular, (and “anfusuhumā”), using the plural form for the dual of masculine and feminine; from some of the Arabs [is reported] “nafsāhumā” and “ʿaynāhumā”;"},
    {"type": "matn",
     "ar": "(و«أنفسهم») في جمع المذكر العاقل (و«أنفسهن») في جمع المؤنث وغير العاقل من المذكر.",
     "en": "(and “anfusuhum”) for the plural of the rational masculine, (and “anfusuhunna”) for the plural of the feminine and of the non-rational masculine."},
    {"type": "matn",
     "ar": "(والثاني) لما سمي «النفس والعين» أولين تغليبا كالقمرين، سمي الثالث ثانيا (للمثنى «كلاهما») للمذكر (و«كلتاهما») للمؤنث.",
     "en": "(The second): since “al-nafs” and “al-ʿayn” were called “the first two” by predominance (taghlīb), as with “the two moons” [for sun and moon], the third was called “the second”: (is for the dual: “kilāhumā”) for the masculine (and “kiltāhumā”) for the feminine."},
    {"type": "matn",
     "ar": "(والباقي) بعد الثلاثة المذكورة (لغير المثنى) مفردا كان أو جمعا (باختلاف الضمير) العائد إلى المتبوع المؤكد",
     "en": "(The rest), after the three mentioned, (are for what is not dual), whether singular or plural, (with variation of the pronoun) referring to the corroborated word followed"},
    {"type": "matn",
     "ar": "(في «كله»[[٥]]) نحو: «قرأت الكتاب كله» (و«كلها») نحو: «قرأت الصحيفة كلها» (و«كلهم») نحو: «اشتريت العبيد كلهم» (و«كلهن») نحو: «طلقت النساء كلهن».",
     "en": "(in “kulluhu”), as in “I read the book, all of it”, (“kulluhā”), as in “I read the page, all of it”, (“kulluhum”), as in “I bought the slaves, all of them”, (and “kulluhunna”), as in “I divorced the women, all of them”."},
    {"type": "matn",
     "ar": "(و) باختلاف (الصيغ في) الكلمات (البواقي) وهي: «أجمع[[٦]]، وأكتع وأبتع وأبصع» بالمهملة أو المعجمة تقول: («أجمع») في المذكر الواحد (و«جمعاء») في المؤنث",
     "en": "(And) with variation of (the forms in the remaining) words, namely “ajmaʿ”, “aktaʿ”, “abtaʿ” and “abṣaʿ”, with the undotted or the dotted letter; you say (“ajmaʿ”) for the masculine singular, (and “jamʿāʾ”) for the feminine …"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "لاشتمال كل منها على خروج من النقصان، وعلى تمام تناسب العموم المستلزم لتمام النسبة.",
     "en": "Because each of them involves a passing beyond deficiency, and a completeness that suits generality, which entails the completeness of the attribution."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "يعني: جعلا عامين لشمولهما الواحد والاثنين والزيادة والمذكر والمؤنث.",
     "en": "He means: they were made general because they cover the singular, the dual, more than two, the masculine and the feminine."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "وهذا أصل في كل مضاف إلى ضمير التثنية مع الاتصال التام بين المضاف والمضاف إليه لكراهة اجتماع التثنيتين مع كل اتصالهما لفظا ومعنى،",
     "en": "This is a principle for every noun annexed to a dual pronoun where the connection between the annexed noun and the noun it is annexed to is complete, because of the dislike of combining two duals with their full connection in wording and meaning."},
    {"type": "pair",
     "ar": "فيقال: نفسا زيد وعمرو وغلاماهما، ولا يقال: نفساهما بل أنفسهما.",
     "en": "So one says “nafsā Zaydin wa-ʿAmrin” and “ghulāmāhumā”, but one does not say “nafsāhumā”; rather, “anfusuhumā”."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "والأول أولى لكراهتهم اجتماع تثنيتين حيث تأكد اتصالهما لفظا ومعنى.",
     "en": "The first is preferable, because of their dislike of combining two duals where their connection in wording and meaning is strong."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "وكذا في جميعه.",
     "en": "Likewise in “jamīʿuhu”."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "لا دلالة له على الاجتماع عند الجمهور خلافا للمازني والمبرد، كذا في الرضي.",
     "en": "According to the majority it does not indicate being together, contrary to al-Māzinī and al-Mubarrad; so in al-Raḍī."},
]
