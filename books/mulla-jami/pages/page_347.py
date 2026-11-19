# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 347 (printed ٣٤٦)."""

PAGE_NUMBER = 347
PRINTED_PAGE = "٣٤٦"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «… (و«جمعاء») في المؤنث» from the foot of PDF p. 346.
    {"type": "matn",
     "ar": "الواحدة أو الجمع[[١]] بتأويل الجماعة و(«أجمعون») في جمع المذكر (و«جمع») في جمع المؤنث[[٢]]،",
     "en": "… singular, or for the plural taken in the sense of “the group”; (“ajmaʿūna”) for the masculine plural, (and “jumaʿ”) for the feminine plural."},
    {"type": "matn",
     "ar": "وكذا «أكتع، كتعاء، أكتعون كتع»، و«أبتع، بتعاء، أبتعون، بتع»، و«أبصع، بصعاء، أبصعون، بصع».",
     "en": "Likewise “aktaʿ, katʿāʾ, aktaʿūna, kutaʿ”; “abtaʿ, batʿāʾ, abtaʿūna, butaʿ”; and “abṣaʿ, baṣʿāʾ, abṣaʿūna, buṣaʿ”."},
    {"type": "matn",
     "ar": "(ولا يؤكد بـ«كل» و«أجمع» إلا ذو أجزاء) مفردا كان أو جمعا؛ إذ الكلية والاجتماع لا يتحققان إلا فيه، ولا حاجة إلى ذكر الأفراد[[٣]]؛",
     "en": "(Only what has parts is corroborated by “kull” and “ajmaʿ”), whether singular or plural, since totality and togetherness are realized only in it; and there is no need to mention individual members,"},
    {"type": "matn",
     "ar": "لأن الكلي ما لم يلاحظ أفراده مجتمعة ولم تصر أجزاء، لا يصح تأكيده بـ«كل وأجمع»،",
     "en": "because a universal, so long as its members are not considered together and have not become parts, cannot be corroborated by “kull” and “ajmaʿ”."},
    {"type": "matn",
     "ar": "ويجب أن تكون تلك الأجزاء بحيث (يصح افتراقها حسا) كأجزاء القوم (أو حكما) كأجزاء العبد، ليكون في التأكيد بـ«كل وأجمع» فائدة",
     "en": "Those parts must be such that (their separation is valid, physically), as with the parts of a people, (or by status), as with the parts of a slave, so that corroboration by “kull” and “ajmaʿ” has a use,"},
    {"type": "matn",
     "ar": "(نحو: «أكرمت القوم كلهم»، و«اشتريت العبد كله») فإن العبد قد يتجزئ في الاشتراء، فيصح تأكيده بـ«كله» ليفيد الشمول",
     "en": "(as in “I honoured the people, all of them” and “I bought the slave, all of him”): a slave may be divided in purchase, so his corroboration by “kullahu” is valid, conveying comprehensiveness;"},
    {"type": "matn",
     "ar": "(بخلاف «جائني زيد كله») لعدم صحة افتراق أجزائه لا حسا ولا حكما[[٤]] في حكم المجيء.",
     "en": "(unlike “jāʾanī Zaydun kulluhu”) (Zayd came to me, all of him), because the separation of his parts is not valid, neither physically nor by status, with respect to the ruling of coming."},
    {"type": "matn",
     "ar": "(وإذا أكد الضمير المرفوع المتصل) بارزا كان أو مستكنا (بالنفس والعين) أي: إذا أريد تأكيده بهما (أكد) ذلك الضمير[[٥]] أولا (بمنفصل) ثم بـ«النفس أو العين»",
     "en": "(When the connected nominative pronoun is corroborated), whether visible or latent, (by al-nafs and al-ʿayn), that is, when its corroboration by them is intended, that pronoun (is corroborated) first (by a separate pronoun), then by al-nafs or al-ʿayn,"},
    {"type": "matn",
     "ar": "(نحو: «ضربت أنت نفسك») فـ«نفسك» تأكيد للتاء الضمير بعد تأكيده بمنفصل وهو «أنت»؛",
     "en": "(as in “ḍarabta anta nafsuka”) (you yourself struck): “nafsuka” is a corroboration of the pronoun tāʾ after its corroboration by a separate pronoun, namely “anta”;"},
    {"type": "matn",
     "ar": "إذ لولا ذلك لالتبس التأكيد بالفاعل إذا وقع تأكيدا للمستكن نحو: «زيد أكرمني هو نفسه»،",
     "en": "for otherwise the corroborative would be confused with the agent when it corroborates a latent pronoun, as in “Zaydun akramanī huwa nafsuhu” (Zayd honoured me, he himself):"},
    {"type": "matn",
     "ar": "فلو لم يؤكد الضمير المستكن في «أكرمني» بقوله: «هو» ويقال: «زيد أكرمني نفسه» لالتبس «نفسه» الذي هو التأكيد بالفاعل،",
     "en": "had the latent pronoun in “akramanī” not been corroborated by “huwa”, and one said “Zaydun akramanī nafsuhu”, then “nafsuhu”, which is the corroborative, would be confused with the agent."},
    {"type": "matn",
     "ar": "ولما وقع الالتباس في هذه الصورة أجري بقية الباب عليه.",
     "en": "Since the confusion arises in this case, the rest of the category was treated in the same way."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "أي: الجمع الذي يجعل في حكم الواحدة، وهو غير الجمع المذكر السالم.",
     "en": "That is, the plural that is given the status of a feminine singular, which is other than the sound masculine plural."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "وما في حكمه من جمع المذكر الغير العاقل. وجوز الأندلسي في العاقل الغير السالم أيضا.",
     "en": "And what has its status, namely the plural of the non-rational masculine. Al-Andalusī also permitted it for the rational [masculine] in a plural that is not sound."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "بل لا يصح ذكرها؛ لأنه يفيد جواز جاءني الإنسان كله من غير أن يراد به الإناس،",
     "en": "Rather, mentioning them is not valid, because it would imply the permissibility of “jāʾanī al-insānu kulluhu” (man came to me, all of him) without “people” (al-unās) being meant by it."},
    {"type": "pair",
     "ar": "فقد أفسد من أصلح قول المصنف: ذوا أجزاء بتأويله بذي متعدد أفرادا كان أو أجزاء.",
     "en": "So whoever “corrected” the author’s words “what has parts” by interpreting it as “what is multiple, whether in members or in parts” has spoiled them."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "أي: افتراق حس أو افتراق حكم.",
     "en": "That is, physical separation or separation by status."},
    {"type": "pair",
     "ar": "والظاهر أنه لا يكفي الافتراق الحسي بدون الافتراق الحكمي حتى لو كان ذو أجزاء يصح افتراقها حسا ولم يصح افتراقها حكما وحالا لم يصح توكيده بكل وأجمع، فالمعيار الافتراق الحكمي.",
     "en": "What is apparent is that physical separation does not suffice without separation by status, so that if something with parts admits physical separation of its parts but not separation by status and circumstance, its corroboration by “kull” and “ajmaʿ” would not be valid. The criterion, then, is separation by status."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "كأنه دل عليه المصنف بالمثال.",
     "en": "It is as if the author indicated it by the example."},
    {"type": "pair",
     "ar": "ولا يخفى أنه لا وجه للفصل بين هذا الحكم وبين بيان النفس والعين كما لا وجه للفصل بين قوله: ولا يؤكد بكل وأجمع. وقوله: وأكتع وأخواه مع شدة اتصال أكتع وأخويه بأجمع وشدة اتصال هذا الحكم بالحكم السابق؛",
     "en": "It is not hidden that there is no reason to separate this ruling from the account of al-nafs and al-ʿayn, just as there is no reason to separate his words “Only what has parts is corroborated by kull and ajmaʿ” from his words “aktaʿ and its two sisters”, given the close connection of aktaʿ and its two sisters with ajmaʿ, and the close connection of this ruling with the preceding ruling;"},
    {"type": "pair",
     "ar": "إذ يعلم منه أن الحكم السابق يشمل أكتع وأخويه، ولهذا اقتصر فيه على ذكر أجمع.",
     "en": "for it is known from it that the preceding ruling covers aktaʿ and its two sisters, and this is why he mentioned only ajmaʿ in it."},
]
