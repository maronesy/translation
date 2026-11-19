# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 144 (printed ١٤٣)."""

PAGE_NUMBER = 144
PRINTED_PAGE = "١٤٣"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    {"type": "matn",
     "ar": "الظاهر مفعولا له، فيكونان متفقين في اقتضاء المفعولية (مثل: «ضربت وأكرمت زيدا»).",
     "en": "…overt [noun] to be its object, so that the two agree in requiring objecthood (as in: “I struck and honored Zayd”—ḍarabtu wa-akramtu Zaydan)."},
    {"type": "matn",
     "ar": "٣- (و) قد يكون تنازعهما (في الفاعلية والمفعولية) وذلك يكون على وجهين[[١]]:",
     "en": "3. (And) their contention may be (in agency and objecthood—fī al-fāʿiliyya wa-l-mafʿūliyya); and that occurs in two ways:"},
    {"type": "matn",
     "ar": "أحدهما: أن يقتضي كل منهما فاعلية اسم ظاهر، ومفعولية اسم ظاهر آخر، فيكونان متفقين في ذلك الاقتضاء،",
     "en": "The first of them: that each of them requires the agency of one overt noun and the objecthood of another overt noun, so that the two agree in that requirement,"},
    {"type": "matn",
     "ar": "مثل: «ضرب وأهان زيد عمرا»، وليس هذا قسما ثالثا من التنازع[[٢]]، بل هو اجتماع القسمين الأولين.",
     "en": "as in: “Zayd struck and humiliated ʿAmr” (ḍaraba wa-ahāna Zaydun ʿAmran). This is not a third division of tanāzuʿ; rather it is the combination of the first two divisions."},
    {"type": "matn",
     "ar": "وثانيهما: أن يقتضي أحد الفعلين فاعلية اسم ظاهر، والآخر مفعولية ذلك الاسم الظاهر بعينه.",
     "en": "The second of them: that one of the two verbs requires the agency of an overt noun, and the other the objecthood of that very same overt noun."},
    {"type": "matn",
     "ar": "ولا شك في اختلاف اقتضاء الفعلين في هذه الصورة. وهذا هو القسم الثالث المقابل للأولين.",
     "en": "There is no doubt that the requirements of the two verbs differ in this case. This is the third division, set over against the first two."},
    {"type": "matn",
     "ar": "فقوله: (مختلفين[[٣]]) لتخصيص هذه الصورة بالإرادة،",
     "en": "So his words (differing—mukhtalifayn) serve to single out this case as the one intended;"},
    {"type": "matn",
     "ar": "يعني: «قد يكون تنازع الفعلين[[٤]] واقعا في الفاعلية والمفعولية حال كون الفعلين مختلفين في الاقتضاء»،",
     "en": "he means: “the contention of the two verbs may occur in agency and objecthood while the two verbs differ in [their] requirement,”"},
    {"type": "matn",
     "ar": "وذلك لا يتصور إلا إذا كان الاسم الظاهر المتنازع فيه واحدا.",
     "en": "and that is inconceivable unless the overt noun contended over is a single one."},
    {"type": "matn",
     "ar": "وإنما لم يورد مثالا للقسم الثالث؛ لأنه إذا أخذ فعل من المثال الأول، وفعل من المثال الآخر حصل مثال القسم الثالث،",
     "en": "He gave no example of the third division only because, if one verb is taken from the first example and one verb from the other example, an example of the third division results;"},
    {"type": "matn",
     "ar": "وذلك يتصور على وجوه كثيرة، مثل: «ضربني وضربت زيدا»، و«أكرمني وأكرمت زيدا»، و«ضربني وأكرمت زيدا»، و«أكرمني وضربت زيدا»،",
     "en": "and that can be conceived in many ways, such as: “Zayd struck me and I struck [him]” (ḍarabanī wa-ḍarabtu Zaydan), “Zayd honored me and I honored [him],” “Zayd struck me and I honored [him],” and “Zayd honored me and I struck [him],”"},
    {"type": "matn",
     "ar": "وغير ذلك مما يكون الاسم الظاهر مرفوعا.",
     "en": "and other [cases] in which the overt noun is in the nominative."},
    {"type": "matn",
     "ar": "(فيختار) النحاة (البصريون[[٥]] إعمال) الفعل (الثاني) لقربه[[٦]] مع تجويز إعمال الأول.",
     "en": "(Then the Baṣran) grammarians (choose to make) the (second) verb (govern—fa-yakhtāru al-baṣriyyūn iʿmāl al-thānī), because of its proximity, while allowing the first to be made to govern."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "وله وجه آخر أيضا غير ما ذكر من الوجهين، وهو أن يقتضي أحد الفعلين الفاعل والمفعول، والآخر المفعول فقط،",
     "en": "It also has another way besides the two mentioned, namely that one of the two verbs requires the agent and the object, and the other the object only,"},
    {"type": "pair",
     # REVIEW: printed «وحبست» (not «وحسبت»); transcribed as printed.
     "ar": "نحو: «ضربت وحبست زيدا منطلقا» إن كان النزاع في «زيدا منطلقا» بأن يكون فاعلا ومفعولا للأول، أو يكون مفعولا للثاني.",
     "en": "as in: “I struck, and I detained Zayd setting off,” if the contention is over “Zaydan munṭaliqan,” in that it would be agent and object for the first, or object for the second."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "بل اجتماع القسمين الأولين، فإن وحدة المقسم معتبرة في جميع التقسيمات لئلا يخل في الحصر اجتماع القسمين.",
     "en": "Rather [it is] the combination of the first two divisions; for the unity of the thing divided (al-maqsam) is taken into account in all divisions, lest the combination of two divisions disrupt the exhaustiveness [of the division]."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "حال، والعامل فيه معنى فعل يستفاد من الضمير المستتر في قوله: فقد يكون لرجوعه إلى تنازع الفعلين المدلول عليه بقوله: إذا تنازع الفعلان،",
     "en": "[It is] a ḥāl, and what governs it is the meaning of a verb derived from the pronoun concealed in his words “then it may be,” because [that pronoun] refers back to the contention of the two verbs indicated by his words “when the two verbs contend,”"},
    {"type": "pair",
     "ar": "لا أن العامل نفس الضمير، فيكون هذا التركيب مثل «هذا زيد قائما» في أن العامل فيه فعل توهمي.",
     "en": "not that the governor is the pronoun itself; so this construction is like “This is Zayd, standing” (hādhā Zaydun qāʾiman) in that what governs it is a notionally supposed (tawahhumī) verb."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "نبه على حالية مختلفين، وعلى ذي الحال والعامل أيضا، وهو معنى الفعل المستفاد من الضمير الراجع إلى المصدر لا نفس الضمير كما يتبادر منه؛",
     "en": "He drew attention to “mukhtalifayn” being a ḥāl, and also to the possessor of the ḥāl (dhū al-ḥāl) and the governor, which is the meaning of the verb derived from the pronoun referring back to the verbal noun, not the pronoun itself as might first be understood from it;"},
    {"type": "pair",
     "ar": "لأن الضمير لا يعمل ولو رجع إلى نفس المصدر.",
     "en": "because a pronoun does not govern, even if it refers back to the verbal noun itself."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "لم يقل: فالمختار إعمال الثاني خلافا للكوفيين مع أنه أخصر وبعبارته في البيان أوفق؛",
     "en": "He did not say “the preferred [course] is to make the second govern, contrary to the Kūfans,” although that is more concise and more in keeping with his phrasing in the exposition;"},
    {"type": "pair",
     "ar": "لأنه حينئذ لا يعلم أن المختار عند الكوفيين الأول لاحتمال المساواة.",
     "en": "because in that case it would not be known that the preferred [course] according to the Kūfans is the first, owing to the possibility of [their holding] equality."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "أي: قربه مع مساواة العاملين في القوة، فينتقض بمثل: زيد يضرب ومكرم عمرا.",
     "en": "That is: its proximity together with the equality of the two governors in strength; so it is contradicted by such as: “Zayd strikes and is honoring ʿAmr.”"},
]
