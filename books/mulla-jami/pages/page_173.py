# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 173 (printed ١٧٢)."""

PAGE_NUMBER = 173
PRINTED_PAGE = "١٧٢"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    {"type": "matn",
     "ar": "في التركيب[[١]] الذي التزم (في موضعه) أي: في موضع الخبر (غيره) أي: غير الخبر.",
     "en": "…in the construction in which there has been made binding (in its place—fī mawḍiʿihi), that is: in the place of the predicate, (something other than it—ghayruhu), that is: other than the predicate."},
    {"type": "matn",
     "ar": "وذلك في أربع أبواب[[٢]] على ما ذكره المصنف:",
     "en": "That is in four categories, according to what the author mentioned:"},
    {"type": "matn",
     "ar": "أولها: المبتدأ الذي بعد «لولا»[[٣]] (مثل: «لولا زيد لكان كذا») أي: «لولا زيد موجود»؛",
     "en": "The first of them: the subject that comes after “lawlā” (as in: “Were it not for Zayd, such-and-such would have been”—lawlā Zaydun la-kāna kadhā), that is: “Were it not that Zayd exists”;"},
    {"type": "matn",
     "ar": "لأن «لولا» لامتناع الشيء لوجود غيره، فيدل على الوجود، وقد التزم في موضع الخبر جواب «لولا»،",
     "en": "because “lawlā” is for the non-occurrence of a thing owing to the existence of another, so it indicates existence; and the apodosis (jawāb) of “lawlā” has been made binding in the place of the predicate;"},
    {"type": "matn",
     "ar": "فيجب حذفه لقيام قرينة، والتزام قائم مقامه، هذا إذا كان الخبر عاما.",
     "en": "so its elision is obligatory, because an indicator is present and something standing in its place has been made binding. This is when the predicate is general (ʿāmm)."},
    {"type": "matn",
     "ar": "وأما إذا كان خاصا فلا يجب حذفه[[٤]] كما في قوله:",
     "en": "When it is specific (khāṣṣ), its elision is not obligatory, as in the poet’s words:"},
    {"type": "verse",
     "ar": "ولولا الشعر بالعلماء يزري        لكنت اليوم أشعر من لبيد",
     "en": "“Were it not that poetry demeans scholars, I would today be a greater poet than Labīd.”"},
    {"type": "matn",
     "ar": "هذا على مذهب البصريين.",
     "en": "This is according to the doctrine of the Baṣrans."},
    {"type": "matn",
     "ar": "وقال الكسائي: الاسم بعدها فاعل لفعل مقدر، أي: «لولا وجد زيد».",
     "en": "Al-Kisāʾī said: the noun after it is the agent (fāʿil) of an implied verb, that is: “were it not that Zayd was found.”"},
    {"type": "matn",
     "ar": "وقال الفراء: «لولا» هي الرافعة[[٥]] للاسم الذي بعدها.",
     "en": "Al-Farrāʾ said: “lawlā” is itself what puts the noun after it in the nominative."},
    {"type": "matn",
     "ar": "وثانيها: كل مبتدأ كان مصدرا صورة[[٦]] أو بتأويله منسوبا إلى الفاعل[[٧]] أو المفعول أو كليهما، وبعده حال[[٨]]،",
     "en": "The second of them: every subject that is a verbal noun (maṣdar) in form, or by interpretation as one, attributed to the agent, to the object or to both, and followed by a circumstantial qualifier (ḥāl);"},
    {"type": "matn",
     "ar": "أو كان اسم تفضيل مضافا إلى ذلك المصدر،",
     "en": "or [every subject] that is an elative (ism tafḍīl) annexed to such a verbal noun."},
    {"type": "matn",
     "ar": "وذلك مثل: «ذهابي راجلا» و«ضرب زيد قائما» إذا كان زيد مفعولا به (و) مثل: («ضربي زيدا",
     "en": "That is as in: “my going on foot” (dhahābī rājilan) and “the beating of Zayd standing” (ḍarbu Zaydin qāʾiman), when Zayd is the direct object; (and) as in: (“my beating Zayd…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "الأظهر بحسب اللفظ أن يقال: أي: في خبر، وإلا لزم خلو الجملة عن العائد بحسب الظاهر؛",
     "en": "The more evident [gloss] in terms of wording is to say: “that is: in a predicate”; otherwise the clause would, on its face, lack a resumptive pronoun (ʿāʾid);"},
    {"type": "pair",
     "ar": "لأن ضمير «في موضعه» و«غيره» راجع إلى الخبر.",
     "en": "because the pronoun of “in its place” and “other than it” refers back to the predicate."},
    {"type": "pair",
     "ar": "وإنما قلنا: بحسب الظاهر؛ لأن الذهن ينساق من الخبر إلى كونه واقعا في التركيب، فيغني غناء الضمير.",
     "en": "We said “on its face” only because the mind passes from the predicate to its occurring in the construction, so it serves in place of the pronoun."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "لا يقال: هناك قسم آخر، وهو ما إذا كان الخبر ظرفا، فإن متعلقه خبر، وهو واجب الحذف؛",
     "en": "It is not to be said: there is another category, namely when the predicate is an adverbial (ẓarf), for what it attaches to (mutaʿallaq) is the predicate, and its elision is obligatory;"},
    {"type": "pair",
     "ar": "لأنا نقول: الخبر بحسب الظاهر، بل بحسب الحقيقة ليس إلا الظرف.",
     "en": "for we say: the predicate, on its face and indeed in reality, is nothing but the adverbial."},
    {"type": "pair",
     "ar": "والتقدير ليس إلا لرعاية أمر لفظي، فليس هو من باب حذف الخبر والتزام غيره مسده.",
     "en": "The supposition [of an implied element] is only to observe a matter of wording; so it does not belong to the category of eliding the predicate and making binding something else in its place."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "الأولى أن يقول: المبتدأ الذي بعد «لولا» وخبره عام ليستغنى عن قوله: هذا إذا كان الخبر عاما،",
     "en": "It would have been better to say: “the subject that comes after ‘lawlā’ whose predicate is general,” so that his words “this is when the predicate is general” would be unnecessary."},
    {"type": "pair",
     "ar": "وكأنه اختار ما اختار تنبيها على أن تعيين النحاة الضابطة الأولى قاصر لا بد من تقييده.",
     "en": "It seems he chose what he chose to point out that the grammarians’ specification of the first rule is deficient and must be qualified."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "لعدم دلالة «لولا» عليه، ولو دل بالقرينة الخارجة جاز الحذف بلا وجوب.",
     "en": "Because “lawlā” does not indicate it; and if it were indicated by an external indicator, elision would be permissible without being obligatory."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "ولا يخفى أنه لا بد من القول بحذف مسند الكلام،",
     "en": "It is not hidden that one must hold that the predicand (musnad) of the utterance is elided;"},
    {"type": "pair",
     "ar": "فحينئذ إن كان خبرا فيلزم كون المسند إليه معمولا لا لعامل لفظي دون الخبر.",
     "en": "so then, if it is a predicate, it follows that the subject of predication (musnad ilayhi) is governed not by a verbal governor (lā li-ʿāmil lafẓī), as distinct from the predicate."},  # REVIEW: «معمولا لا لعامل لفظي دون الخبر» is elliptical; rendered literally

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "الأولى كان مصدرا أو مؤولا به، فإن المتبادر من الصدر صورة ألا يكون مصدرا حقيقة، فافهم.",  # REVIEW: printed «الصدر»; perhaps for «المصدر» (the matn has «مصدرا صورة»)
     "en": "Better: “[that] is a verbal noun or interpreted as one”; for what first comes to mind from “in form” is that it is not a verbal noun in reality. So understand."},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "قال الرضي: بدل منسوبا مضافا إلى الفاعل أو المفعول أو إلى الفاعل والمفعول نحو: تضاربنا.",
     "en": "Al-Raḍī said, instead of “attributed”: “annexed to the agent or the object, or to the agent and the object,” as in: “our beating one another” (taḍārubunā)."},

    # ---------------- Footnote 8 ----------------
    {"type": "note", "num": "٨"},
    {"type": "pair",
     "ar": "ويجب في هذه الحال الواو إذا كانت جملة اسمية.",
     "en": "The wāw is obligatory with this ḥāl when it is a nominal clause."},
    {"type": "pair",
     "ar": "قال عبد الغفور: مفردة كانت أو جملة اسمية كانت أو فعلية، والاسمية يجب معها الواو على الأصح.",
     "en": "ʿAbd al-Ghafūr said: [whether] it is a single word or a clause, nominal or verbal; and with the nominal one the wāw is obligatory according to the sounder view."},
]
