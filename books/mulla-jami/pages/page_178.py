# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 178 (printed ١٧٧)."""

PAGE_NUMBER = 178
PRINTED_PAGE = "١٧٧"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    {"type": "matn",
     "ar": "التعريف بمثل: «يقوم» في قولنا: «إن زيدا يقوم أبوه»،",
     "en": "…the definition [is not contradicted] by such as “yaqūmu” in our saying: “Zayd—his father stands” (inna Zaydan yaqūmu abūhu),"},
    {"type": "matn",
     "ar": "فإن «يقوم» ههنا من حيث إسناده إلى «أبوه» ليس مما يدخل عليه «إن» بهذا المعنى، بل إنما دخل على جملة هي «يقوم أبوه»،",
     "en": "for “yaqūmu” here, inasmuch as it is predicated of “abūhu,” is not among the things on which “inna” enters in this sense; rather, it has entered only upon a sentence, which is “yaqūmu abūhu.”"},
    {"type": "matn",
     "ar": "فلا يحتاج إلى أن يجاب عنه: بأن المراد بالمسند المسند إلى أسماء هذه الحروف، ويلزم منه استدراك قوله: «بعد دخول هذه الحروف»،",
     "en": "So there is no need to answer it by [saying] that what is meant by “the predicate” (al-musnad) is that which is predicated of the nouns of these particles—from which it would follow that his words “after the entry of these particles” are redundant (istidrāk);"},
    {"type": "matn",
     "ar": "ولا إلى أن يجاب: بأن المراد بالمسند الاسم المسند، فيحتاج إلى تأويل الجملة بالاسم حيث يكون خبرها جملة مثل: «إن زيدا يقوم» مؤول بقائم.",
     "en": "nor to answer [by saying] that what is meant by “the predicate” is the predicated noun, so that one would need to interpret the sentence as a noun wherever its predicate is a sentence—as in “inna Zaydan yaqūmu,” which is interpreted as “qāʾim.”"},
    {"type": "matn",
     "ar": "(مثل) «قائم» في («إن زيدا قائم»)، فإنه المسند بعد دخول هذه الحروف.",
     "en": "(Such as) “qāʾim” in (“Zayd is standing,” inna Zaydan qāʾimun), for it is the predicate after the entry of these particles."},
    {"type": "matn",
     "ar": "(وأمره كأمر خبر المبتدأ) أي: حكمه كحكم خبر المبتدأ في أقسامه من كونه مفردا وجملة ونكرة ومعرفة،",
     "en": "(And its status is like the status of the predicate of the subject [khabar al-mubtadaʾ]); that is, its rule is like the rule of the predicate of the subject in its divisions—its being a single word (mufrad) or a sentence, indefinite or definite—"},
    {"type": "matn",
     "ar": "وفي أحكامه من كونه واحدا ومتعددا ومثبتا ومحذوفا،",
     "en": "and in its rulings—its being single or multiple, stated or elided—"},
    {"type": "matn",
     "ar": "وفي شرائطه من أنه إذا كان جملة فلا بد من عائد، ولا يحذف إلا إذا علم،",
     "en": "and in its conditions—that, if it is a sentence, a resumptive element (ʿāʾid) is indispensable, and that it is not elided unless it is known."},
    {"type": "matn",
     "ar": "والمراد أن أمره كأمره بعد أن صح كونه خبرا بوجود شرائطه وانتفاء موانعه،",
     "en": "What is meant is that its status is like its [the subject’s predicate’s] status once its being a predicate has become valid through the presence of its conditions and the absence of its impediments;"},
    {"type": "matn",
     "ar": "ولا يلزم من ذلك أن كل ما يصح أن يكون خبرا للمبتدأ يصح أن يقع خبرا لباب «إن»،",
     "en": "and it does not follow from this that everything that can validly be the predicate of a subject can validly occur as the predicate of the chapter of “inna,”"},
    {"type": "matn",
     "ar": "حتى يرد أنه يجوز أن يقال: «أين زيد؟»[[١]] و«من أبوك؟»، ولا يجوز أن يقال: «إن أين زيدا؟»[[٢]] و«إن من أباك؟».",
     "en": "such that the objection would arise that one may say “Where is Zayd?” (ayna Zaydun?) and “Who is your father?” (man abūka?), whereas one may not say “inna ayna Zaydan?” or “inna man abāka?”"},
    {"type": "matn",
     "ar": "(إلا في تقديمه[[٣]]) أي: ليس أمره كأمر خبر المبتدأ في تقديمه، فإنه لا يجوز تقديمه على الاسم، وقد جاز تقديم الخبر على المبتدأ،",
     "en": "(Except in its being placed first); that is, its status is not like the status of the predicate of the subject with respect to its being placed first, for it may not be placed before the noun [of inna], whereas placing the predicate before the subject is permitted."},
    {"type": "matn",
     "ar": "وذلك لأن هذه الحروف فروع على الفعل في العمل، فأريد أن يكون عملها فرعيا أيضا،",
     "en": "That is because these particles are derivative of the verb in [their] governing (ʿamal), so it was intended that their governing be derivative as well;"},
    {"type": "matn",
     "ar": "والعمل الفرعي للفعل أن يتقدم المنصوب على المرفوع، والأصلي أن يتقدم[[٤]] المرفوع على المنصوب،",
     "en": "and the derivative governing of the verb is that the accusative precede the nominative, while the original [governing] is that the nominative precede the accusative."},
    {"type": "matn",
     "ar": "فلما أعملت العمل الفرعي لم يتصرف في معموليها بتقديم ثانيهما على الأول كما يتصرف في معمولي الفعل، لنقصانها عن درجة الفعل.",
     "en": "So, since they were made to exercise the derivative governing, no free disposal is made of their two governed elements by placing the second of them before the first, as free disposal is made of the two governed elements of the verb, on account of their falling short of the rank of the verb."},

    {"type": "rule"},

    # ---------------- Orphan continuation (tail of footnote ٧ from p.177) ----------------
    # Unnumbered continuation, so the note count below exceeds the matn markers by one.
    {"type": "note", "num": ""},
    {"type": "pair",
     "ar": "المكفوفة بـ«ما» أو بعد «إن» المخففة الملغاة.",
     "en": "…[the “inna”] restrained by “mā,” or after the lightened, inoperative “in.”"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "اضربه، ولا يجوز أن يقال: إن زيدا اضربه.",
     "en": "[And “Zayd,] strike him” (iḍribhu); but one may not say: “inna Zaydan iḍribhu.”"},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "لأن الاستفهام ينافي التحقيق.",
     "en": "Because interrogation is incompatible with affirmation (taḥqīq)."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "حق العبارة أن يقال: إلا في التقديم؛ لأنه استثناء عن وجوه الشبه.",
     "en": "The proper wording would be to say: “except in placing first” [without the pronoun]; because it is an exception from the respects of resemblance."},
    {"type": "pair",
     "ar": "ووجه الشبه يجب أن يكون مشتركا بين المشبه والمشبه به، والقول برجوع الضمير إلى المتكلم بعيد.",
     "en": "The respect of resemblance must be shared between the thing compared and that to which it is compared; and the view that the pronoun refers back to the speaker is far-fetched."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "كما مر في قوله: والأصل أن يلي الفعل.",
     "en": "As has passed in his words: “The default is that it [the agent] immediately follow the verb.”"},
]
