# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 274 (printed ٢٧٣)."""

PAGE_NUMBER = 274
PRINTED_PAGE = "٢٧٣"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «فإنه إذا قصد تثنيته أو جمعيته لا» from the foot of PDF p. 273.
    {"type": "matn",
     "ar": "يلزم أن يثنى ذلك الجنس[[١]] أو يجمع، بل يكفي أن يؤتى به مفردا لصحة إطلاقه على القليل والكثير، فلا حاجة إلى تثنيته وجمعه",
     "en": "…necessary that that generic noun be put in the dual or the plural; rather, it suffices to bring it in the singular, since it can properly be applied to few and many, so there is no need for its dual or plural,"},
    {"type": "matn",
     "ar": "نحو: «طاب زيد علما، والزيدان علما، والزيدون علما»",
     "en": "as in “Zayd is good in knowledge, the two Zayds are good in knowledge, and the Zayds are good in knowledge,”"},
    {"type": "matn",
     "ar": "(إلا أن يقصد) بالتمييز الذي هو الجنس (الأنواع) من حيث امتيازاتها النوعية،",
     "en": "(unless) by the specification that is a generic noun (the species are intended), in respect of their specific distinctions;"},
    {"type": "matn",
     "ar": "فإنه لا بد حينئذ من تثنيته أو جمعه نحو: «طاب الزيدان علمين، والزيدون علوما» إذا أريد أن متعلق الطيب من كل من الزيدين والزيدين نوع آخر من العلم،",
     "en": "for then its dual or plural is indispensable, as in “The two Zayds are good in two knowledges, and the Zayds in knowledges,” when it is meant that what the goodness of each of the two Zayds and of the Zayds is connected with is a different kind of knowledge;"},
    {"type": "matn",
     "ar": "فإن صيغة المفرد لا يفيد ذلك المعنى.",
     "en": "for the singular form does not convey that meaning."},
    {"type": "matn",
     "ar": "(وإن كان) أي: التمييز (صفة) مشتقة مثل: «لله دره فارسا»، أو مؤولة بها نحو: «كفى زيد رجلا»، فإن معناه: كاملا في الرجولية",
     "en": "(And if it is)—that is, the specification—(an adjective), derived, as in “To Allah [belongs] his milk as a horseman!”, or interpreted as one, as in “Zayd suffices as a man,” whose meaning is: “perfect in manliness,”"},
    {"type": "matn",
     "ar": "(كانت) الصفة (صفة له) أي: لما انتصب عنه لا لمتعلقه؛ لأن الصفة تستدعي موصوفا، والمذكور أولى بالموصوفية،",
     "en": "(then) the adjective (is an adjective of it), that is, of that from which it takes the accusative, not of what is connected with it; because an adjective calls for something qualified, and what is mentioned has the better claim to be the qualified."},
    {"type": "matn",
     "ar": "فإذا قيل: «طاب زيد والدا» كان الوالد زيدا، ولا يحتمل أن يكون والده، بخلاف الاسم نحو: «أبا»",
     "en": "So when it is said “Zayd is good as a parent (wālidan),” the parent is Zayd, and it cannot be his parent—unlike the noun, as in “in respect of father (aban).”"},
    {"type": "matn",
     "ar": "(وطبقه) الواو بمعنى «مع»[[٢]]، والطبق مصدر بمعنى المطابقة، أي: كانت الصفة صفة له مع مطابقتها إياه أو مطابقته إياها،",
     "en": "(And in agreement with it): the wāw has the sense of “with” (maʿa), and ṭibq is a verbal noun meaning agreement (muṭābaqa); that is, the adjective is an adjective of it together with its agreeing with it, or its agreeing with the adjective."},
    {"type": "matn",
     "ar": "ويجوز أن يكون بمعنى اسم الفاعل[[٣]] والواو للعطف على خبر كانت، أي: كانت صفة له ومطابقة إياه[[٤]]،",
     "en": "It may also have the sense of the active participle, with the wāw coordinating with the predicate of “kānat”; that is, it is an adjective of it and agreeing with it."},
    {"type": "matn",
     "ar": "والمراد بالمطابقة الاتفاق في الإفراد والتثنية والجمع والتذكير والتأنيث، لكونها حاملة لضميره",
     "en": "What is meant by agreement is concord in singular, dual and plural, masculine and feminine, because it carries its pronoun."},
    {"type": "matn",
     "ar": "(واحتملت) أي: الصفة المذكورة (الحال[[٥]]) أيضا لاستقامة المعنى على الحال نحو: «طاب زيد فارسا»، أي: من حيث إنه فارس أو حال كونه فارسا، لكن زيادة «من»",
     "en": "(And it admits)—that is, the adjective mentioned—(the circumstantial accusative, ḥāl) as well, because the meaning holds as a ḥāl, as in “Zayd is good as a horseman,” that is, in respect of his being a horseman, or in the state of being a horseman. But the addition of “min”…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "هذا ينافي ما سبق من أن تثنية الجنس وجمعيته لا يخص قصدا للأنواع، بل أمر مشترك بين قصد الأنواع، وقصد الأفراد حتى احتاج إلى التكلف،",
     "en": "This contradicts what preceded, namely that the dual and plural of a generic noun is not particular to intending the species, but is something common to intending the species and intending the individuals—so that he needed a strained interpretation;"},
    {"type": "pair",
     "ar": "بل التعسف بحمل الأنواع على ما يشتمل الأفراد ما أعجل نسيانه بما شيد عن قريب بنيانه.",
     "en": "indeed, the forced reading of taking “species” to include individuals. How quickly he forgot what he had built up so shortly before!"},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "وهي تفيد مشاركة ما بعده لخبر كان من حيث إنه فاعل معنى.",
     "en": "It conveys that what follows it shares with the predicate of “kāna” in being an agent in meaning."},
    {"type": "pair",
     "ar": "ونظيره ما قاله الشيخ الرضي، وهو أن المنصوب في عبارات النحاة في نحو قولهم: شر أهر ذا ناب، إن شرا مبتدأ لفظا فاعل معنى تمييز عن النسبة تقديرا",
     "en": "Its parallel is what Shaykh al-Raḍī said: that the accusative in the grammarians' phrasing about such an expression as “An evil made the fanged one snarl”—“sharrun is a mubtadaʾ in wording, an agent in meaning”—is a specification of the relation by implication;"},
    {"type": "pair",
     "ar": "أي: كائن مبتدأ لفظا بمعنى كائن لفظه مبتدأ، وكائن معناه فاعلا، ومثله كثير في كلامهم.",
     "en": "that is, “being a mubtadaʾ in wording” in the sense of “its wording being a mubtadaʾ,” and “its meaning being an agent.” The like of this is frequent in their speech."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "لا معنى للاقتصار على كونه بمعنى الفاعل مع تجويز كونه مبنيا للمفعول في التوجيه السابق.",
     "en": "There is no sense in restricting it to the meaning of the active participle while allowing it to be passive in the preceding interpretation."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "يعني: الطبق يصح أن يجعل مبنيا للفاعل، ويصح أن يجعل مبنيا للمفعول.",
     "en": "He means: ṭibq may properly be taken as active, and may properly be taken as passive."},
    {"type": "pair",
     "ar": "والأول أظهر لسباق الكلام وسياقه؛ لأنه جعل التمييز مطابقا لما انتصب عنه أو لمتعلقه، فالمناسب أن يجعل الصفة مطابقة له، وإن صح العكس،",
     "en": "The first is more evident from what precedes and follows in the discourse; because he made the specification agree with that from which it takes the accusative or with what is connected with it, so it is fitting to make the adjective agree with it, even if the reverse is correct;"},
    {"type": "pair",
     "ar": "ولكون المتبادر من المصدر المضاف إلى المفعول المبني له.",
     "en": "and because what first comes to mind from a verbal noun annexed to the object is the [verbal noun] built for it."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "لا معنى لحصر الاحتمال في الصفة.",
     "en": "There is no sense in restricting the possibility to the adjective."},
    {"type": "pair",
     "ar": "والحال لا يجب أن يكون مشتقة، بل كل ما دل على هيئة صح أن يقع حالا.",
     "en": "The ḥāl need not be derived; rather, anything that indicates a state may properly occur as a ḥāl."},
]
