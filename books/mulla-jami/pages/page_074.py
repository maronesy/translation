# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 74 (printed ٧٣)."""

PAGE_NUMBER = 74
PRINTED_PAGE = "٧٣"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- Main text (matn) ----------------
    {"type": "matn",
     "ar": "(و) كذا (الجمع المكسر المنصرف)[[١]] أي: الاسم الذي لم يكن بناء الواحد فيه[[٢]] سالما[[٣]]، ولم يكن غير منصرف، كـ«رجال» و«طلبة».",
     "en": "“And” likewise “the fully-declinable broken plural (al-jamʿ al-mukassar al-munṣarif)” — that is, the noun in which the structure of the singular is not left sound (sālim), and which is not imperfectly declinable, such as “rijāl” (men) and “ṭalaba” (students)."},
    {"type": "matn",
     "ar": "فالإعراب في هذين القسمين[[٤]] من الاسم على الأصل من وجهين:",
     "en": "The iʿrāb in these two categories of the noun is in accordance with the original principle (ʿalā al-aṣl) in two respects:"},
    {"type": "matn",
     "ar": "أحدهما: أن الأصل في الإعراب أن يكون بالحركة[[٥]]، والإعراب فيهما بالحركة.",
     "en": "The first: that the original principle in iʿrāb is that it be by a vowel, and the iʿrāb in both of them is by a vowel."},
    {"type": "matn",
     "ar": "وثانيهما: أنه إذا كان الإعراب بالحركة، فالأصل أن يكون بالحركات الثلاث في الأحوال الثلاثة، والإعراب فيهما بالحركات الثلاث في الأحوال الثلاثة، فالإعراب فيهما:",
     "en": "The second: that when the iʿrāb is by a vowel, the original principle is that it be by the three vowels in the three states; and the iʿrāb in both of them is by the three vowels in the three states. So the iʿrāb in both of them is:"},
    {"type": "matn",
     "ar": "١-(بالضمة رفعا) أي: حالة الرفع.",
     "en": "1. “by the ḍamma in the nominative (rafʿ)” — that is, in the state of rafʿ."},
    {"type": "matn",
     "ar": "٢-(والفتحة نصبا) أي: حالة النصب.",
     "en": "2. “and by the fatḥa in the accusative (naṣb)” — that is, in the state of naṣb."},
    {"type": "matn",
     "ar": "٣-(والكسرة جرا) أي: حالة الجر.",
     "en": "3. “and by the kasra in the genitive (jarr)” — that is, in the state of jarr."},
    {"type": "matn",
     "ar": "فنصب قوله: «رفعا، ونصبا، وجرا» على الظرفية، بتقدير مضاف، ويحتمل النصب على الحالية أو المصدرية.",
     "en": "The accusative in his words “rafʿan, naṣban, and jarran” is on account of adverbiality (ẓarfiyya), with an implied muḍāf; and it may [also] be accusative as a circumstantial qualifier (ḥāl) or as an absolute object (maṣdariyya)."},
    {"type": "matn",
     "ar": "فالقسم الأول: مثل: «جاءني رجل»، و«رأيت رجلا»، و«مررت برجل».",
     "en": "The first category: as in “a man came to me” (jāʾanī rajulun), “I saw a man” (raʾaytu rajulan), and “I passed by a man” (marartu bi-rajulin)."},
    {"type": "matn",
     "ar": "والقسم الثاني: مثل: «جاءني طلبة»، و«رأيت طلبة»، و«مررت بطلبة».",
     "en": "The second category: as in “students came to me” (jāʾanī ṭalabatun), “I saw students” (raʾaytu ṭalabatan), and “I passed by students” (marartu bi-ṭalabatin)."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "إنما لم يقل: فالمفرد والجمع المكسر المنصرفين؛ لأنه قصد نوع تلقيب، ولأنه يلزم الفصل بين الصفة وموصوفها بما ليس صفة له، وهو المكسر، أو لتوهم التغليب كما قيل، وهو بعيد جدا؛ لأن مقام الفرق بين المنصرف وغير المنصرف يأبى عن ذلك.",
     "en": "He did not say “the fully-declinable singular and broken plural (al-mufrad wa-l-jamʿ al-mukassar al-munṣarifayn)” because he intended a kind of titling (talqīb); and because it would entail separating the attribute from the thing it qualifies by something that is not an attribute of it — namely, “al-mukassar (broken)”; or [it is avoided] because of the illusion of predominance-by-attraction (taghlīb), as has been said — though this is very far-fetched, since the context of distinguishing between the declinable and the imperfectly-declinable precludes it."},
    {"type": "pair",
     "ar": "ولو لم يأب عن توهم التغليب لم يأب عن توهم المشاكلة في المذكور، فيكون من قبيل قوله تعالى: ﴿وساءت مرتفقا﴾ [الكهف: ٢٩]، في مقابلة وحسنت مرتفقا.",
     "en": "Had it not precluded the illusion of taghlīb, it would not have precluded the illusion of assimilation (mushākala) in what is mentioned, so that it would be of the kind of His words, the Exalted: “and evil is it as a resting-place” (Qurʾān, Sūrat al-Kahf 18:29), in contrast with “and good is it as a resting-place” (wa-ḥasunat murtafaqan)."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "أي: في ذلك الجمع.",
     "en": "That is: in that plural."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "الأظهر أن يقال: الذي لم يكن ملحقا بآخر واحده، واو ونون ولا ألف وتاء ليظهر خروج مثل: سنون وضربات عنه، ويظهر دخول فلك جمعا لفلك فيه.",
     "en": "The more evident [formulation] is to say: that to the end of whose singular there is appended neither a wāw-and-nūn nor an alif-and-tāʾ — so that the exclusion of the likes of “sinūn” (years) and “ḍarabāt” (blows) from it becomes manifest, and so that the inclusion of “fulk” (ships) as a plural for [the singular] “fulk” becomes manifest within it."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "الأولى ذكر هذا القول بعد شرح قوله: بالضمة رفعا، والفتحة نصبا، والكسرة جرا.",
     "en": "The better [course] would have been to mention this statement after explaining his words: “by the ḍamma in the nominative, the fatḥa in the accusative, and the kasra in the genitive.”"},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "ليكون الدال على صفة الشيء كالصفة الدال عليه، ولأنها أخف الدوال. وهذا مراد من قال: أبعاض الحروف، فالاعتراض عليه بأن كونها أبعاضا أمر وهمي، ولو سلم فلا يقتضي الأصالة بحسب الذات لا في الإعراب ليس بشيء.",
     "en": "So that what indicates the attribute of the thing may be like the attribute [itself] that indicates it, and because [the vowels] are the lightest of indicators. This is what is meant by the one who said [the vowels are] “parts of the letters” (abʿāḍ al-ḥurūf); so the objection against him — that their being parts is a notional matter, and that even if it be conceded it does not entail originality either by essence or in iʿrāb — is of no substance."},
]
