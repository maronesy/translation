# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 343 (printed ٣٤٢)."""

PAGE_NUMBER = 343
PRINTED_PAGE = "٣٤٢"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «… يتوهم أن مثل: «ضرب» from the foot of PDF p. 342.
    {"type": "matn",
     "ar": "زيد عمرا وبكر خالدا» من هذا الباب مع أنه ليس منه، لعدم تعدد العامل فيه؛ إذ العامل هو الأول، والثاني تأكيد له،",
     "en": "… Zaydun ʿAmran wa-Bakrun Khālidan” (Zayd struck ʿAmr, and Bakr Khālid) belongs to this category, although it does not, since there is no multiplicity of governor in it: the governor is the first, and the second is a corroboration (taʾkīd) of it."},
    {"type": "matn",
     "ar": "وذلك العطف كما وقع في قولهم: «ما كل سوداء تمرة وبيضاء شحمة»، وفي قول الشاعر:",
     "en": "That conjunction is such as occurs in their saying “mā kullu sawdāʾa tamratan wa-bayḍāʾa shaḥmatan” (not every black thing is a date, nor every white thing a lump of fat), and in the poet’s words:"},
    {"type": "verse",
     "ar": "أكل امرئ تحسبين امرأ[[١]]          ونار توقد بالليل نارا",
     "en": "Do you take every man to be a man, / and every fire kindled by night to be a fire?"},
    {"type": "matn",
     "ar": "فهذا وإن كان بحسب الظاهر جائزا لكنه (لم يجز) عند الجمهور بحسب الحقيقة؛ لأن الحرف الواحد لم يقو أن يقوم مقام عاملين مختلفين",
     "en": "Although this is permitted in outward appearance, it (is not permitted) according to the majority in reality, because a single particle is not strong enough to stand in place of two differing governors,"},
    {"type": "matn",
     "ar": "(خلافا للفراء) فإنه يجوز هذا العطف بحسب الحقيقة كما جاز بحسب الصورة، ولا يؤول الأمثلة الواردة عليها، ولا يقتصر على صورة السماع، بل يعمها وغيرها،",
     "en": "(contrary to al-Farrāʾ), for he permits this conjunction in reality just as it is permitted in form; he does not reinterpret the examples transmitted in it, nor does he restrict it to the form attested by transmission (samāʿ), but extends it to that and to others."},
    {"type": "matn",
     "ar": "وعدم جواز ذلك العطف مع خلاف الفراء جار في جميع المواد عند الجمهور (إلا في نحو: «في الدار[[٢]] زيد والحجرة عمرو») و«إن في الدار زيدا والحجرة عمرا»",
     "en": "The impermissibility of that conjunction, al-Farrāʾ’s disagreement notwithstanding, holds in all cases according to the majority, (except in such as “fī l-dāri Zaydun wa-l-ḥujrati ʿAmrun”) (in the house is Zayd, and in the room ʿAmr) and “inna fī l-dāri Zaydan wa-l-ḥujrati ʿAmran”;"},
    {"type": "matn",
     "ar": "يعني: إلا في صورة تقديم المجرور وتأخير المرفوع أو المنصوب، لمجيئه في كلامهم،",
     "en": "he means: except in the case where the genitive word precedes and the nominative or accusative word follows, because this occurs in their speech;"},
    {"type": "matn",
     "ar": "واقتصر الجواز على صورة السماع؛ لأن ما خالف القياس يقتصر على مورد السماع",
     "en": "and the permission is restricted to the form attested by transmission, because what departs from analogy (qiyās) is restricted to where transmission attests it,"},
    {"type": "matn",
     "ar": "(خلافا لسيبويه) فإنه لا يجوز هذا العطف بحسب الحقيقة في هذه الصورة أيضا، بل يحملها على حذف المضاف وإبقاء المضاف إليه على إعرابه،",
     "en": "(contrary to Sībawayh), for he does not permit this conjunction in reality in this case either; rather, he takes it as an elision of the annexed noun (muḍāf), the noun to which it is annexed (muḍāf ilayhi) keeping its case,"},
    {"type": "matn",
     "ar": "نحو قوله تعالى: ﴿تريدون عرض الدنيا والله يريد الآخرة﴾[[٣]] بجر الآخرة، كما جاز في بعض القراءة، أي: عرض الآخرة.",
     "en": "as in the words of the Exalted: “You desire the goods of this world, and Allah desires the Hereafter”, with al-ākhira in the genitive, as is permitted in one of the readings, that is, “the goods of the Hereafter”."},

    {"type": "section", "ar": "[التأكيد]",
     "en": "The Corroborative (al-Taʾkīd)"},

    {"type": "matn",
     "ar": "(التأكيد: تابع يقرر أمر المتبوع) أي: حاله وشأنه عند السامع، يعني: يجعل حاله ثابتا مقررا عنده",
     "en": "(The corroborative [taʾkīd] is an appositive [tābiʿ] that establishes the matter of the word it follows [matbūʿ]), that is, its state and standing in the hearer’s mind; he means: it makes its state fixed and established for him"},
    {"type": "matn",
     "ar": "(في النسبة) أي: في كونه منسوبا أو منسوبا إليه، فثبت عنده ويتحقق أن المنسوب أو المنسوب إليه في هذه النسبة هو المتبوع لا غير، وذلك:",
     "en": "(in the attribution [nisba]), that is, in its being the thing attributed or that to which it is attributed, so that it is fixed for him and made certain that the thing attributed, or that to which it is attributed, in this attribution is the word followed and nothing else. That is:"},
    {"type": "matn",
     "ar": "إما لدفع ضرر الغفلة عن السامع، أو لدفع ظنه بالمتكلم الغلط، وذلك الدفع يكون",
     "en": "either to ward off from the hearer the harm of inattention, or to ward off his supposing that the speaker has made a slip; and that warding off is …"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "تحسبين وقع بين مفعوليه، فكل منصوب وليس بمرفوع على حذف المفعول الأول لتحسبين؛ لأنه لا يجوز الاقتصار على أحد مفعولي باب «علمت» عند المصنف،",
     "en": "“Taḥsabīna” occurs between its two objects, so “kulla” is accusative, not nominative on the assumption that the first object of taḥsabīna is elided, because according to the author it is not permitted to make do with one of the two objects of verbs of the class of “ʿalimtu”."},
    {"type": "pair",
     "ar": "ونار توقد مضارع التفعل حذف إحدى تائيه، والتوقد لازم ومتعد، وهو ههنا لازم لعدم جواز حذف التاء من المجهول.",
     "en": "In “wa-nārin tawaqqadu”, [tawaqqadu] is the imperfect of the pattern tafaʿʿul with one of its two tāʾs elided; tawaqqud is intransitive and transitive, and here it is intransitive, since the elision of the tāʾ is not permitted in the passive."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "فإنه يتبدل عدم الجواز بالجواز، والمخالفة بالموافقة خلافا لسيبويه، فإنه لا يستثنى.",
     "en": "For [here] impermissibility gives way to permissibility, and disagreement to agreement, contrary to Sībawayh, for he makes no exception."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "سورة الأنفال: ٦٧.",
     "en": "(Qurʾān, Sūrat al-Anfāl 8:67)."},
]
