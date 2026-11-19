# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 524 (printed ٥٢٣)."""

PAGE_NUMBER = 524
PRINTED_PAGE = "٥٢٣"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The commentary text (matn) ----------------
    # Continues «… وإذا قدر الزمان قبله فلا بد هناك من» at the foot of PDF p. 523 (mid-sentence).
    {"type": "matn",
     "ar": "حصول كلام يفيد فائدة تامة، وإلى هذا أشار بقوله: (ومن ثمة) أي: ومن أجل أنه لتوقيت أمر بمدة ثبوت خبرها لفاعلها",
     "en": "…the presence of a statement that conveys a complete benefit; to this he pointed by his words: (and for that reason), that is, because it is for timing a matter by the duration of its predicate’s holding for its agent,"},
    {"type": "matn",
     "ar": "(احتاج إلى) وجود (كلام[[١]]) مستقل بالإفادة (لأنه) حينئذ مع اسمه وخبره (ظرف) والظرف فضلة غير مستقل بالإفادة،",
     "en": "(it needs) the presence of (a statement) independent in conveying benefit, (because it) is then, together with its noun and predicate, (an adverbial [ẓarf]); and the adverbial is a supplementary element (faḍla) not independent in conveying benefit,"},
    {"type": "matn",
     "ar": "مثل: «اجلس ما دام زيد جالسا» أي: اجلس مدة دوام جلوس زيد،",
     "en": "as in “ijlis mā dāma Zaydun jālisan” (sit as long as Zayd is sitting), that is, sit for the duration of the continuance of Zayd’s sitting;"},
    # REVIEW: printed «فما دام لم يشفع ما دام بـ«اجلس» ولم يحصل من المجموع كلام لا يفيد فائدة تامة»; the clause reads oddly (the sense seems to be: as long as «ما دام» is not joined to «اجلس» and no statement arises from the whole, it does not convey a complete benefit). Transcribed as printed; translation follows that apparent sense.
    {"type": "matn",
     "ar": "فما دام لم يشفع ما دام بـ«اجلس» ولم يحصل من المجموع كلام لا يفيد فائدة تامة،",
     "en": "so as long as “mā dāma” is not paired with “ijlis” and a statement does not arise from the whole, it does not convey a complete benefit;"},
    {"type": "matn",
     "ar": "بخلاف الأفعال المصدرة بحرف النفي، فإنها مع أسمائها وأخبارها كلام مستقل بالإفادة، فلا حاجة إلى وجود كلام ورائها.",
     "en": "unlike the verbs headed by a negative particle, for together with their nouns and predicates they are a statement independent in conveying benefit, so there is no need for a statement beyond them."},
    {"type": "matn",
     "ar": "(و«ليس» لنفي مضمون الجملة حالا) أي: في زمان الحال، مثل: «ليس زيد قائما» أي: الآن، وهذا هو مذهب الجمهور.",
     "en": "(And “laysa” is for negating the content of the sentence in the present), that is, in present time, as in “laysa Zaydun qāʾiman” (Zayd is not standing), that is, now; this is the view of the majority."},
    {"type": "matn",
     "ar": "(وقيل) هي لنفي مضمون الجملة (مطلقا) ولذلك تقيد[[٢]] تارة بزمان الحال، كما تقول: «ليس زيد قائما الآن»،",
     "en": "(And it has been said) that it is for negating the content of the sentence (absolutely); for that reason it is restricted at times to present time, as you say “laysa Zaydun qāʾiman al-āna” (Zayd is not standing now),"},
    {"type": "matn",
     "ar": "وتارة بزمان الماضي، نحو: «ليس خلق الله تعالى مثله»، وتارة بزمان المستقبل، نحو قوله تعالى[[٣]]: ﴿ألا يوم يأتيهم ليس مصروفا عنهم﴾[[٤]]، وهذا مذهب سيبويه.",
     "en": "at times to past time, as in “laysa khalaqa Allāhu taʿālā mithlahu” (Allah the Exalted has not created the like of him), and at times to future time, as in His words, the Exalted: “Truly, on the day it comes to them, it will not be averted from them”; this is the view of Sībawayh."},
    {"type": "matn",
     "ar": "(ويجوز تقديم أخبارها) أي: أخبار الأفعال الناقصة (كلها[[٥]] على أسمائها)؛ إذ",
     "en": "(And it is permissible to place their predicates), that is, the predicates of the incomplete verbs, (all of them, before their nouns), since…"},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "سوى ما دخل عليه؛ لأنه مشترك بينه وبين سائر الأفعال الناقصة،",
     "en": "Other than what it enters upon, because that is common to it and the rest of the incomplete verbs;"},
    {"type": "pair",
     "ar": "وقد نبه بقوله: لأنه ظرف على أنه لا بد لهذا الكلام من اشتمال على ما ينصب الظرف.",
     "en": "and by his words “because it is an adverbial” he pointed out that this statement must contain something that puts the adverbial in the accusative."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "فإنه لو كان لنفي الحال يكون التقييد بزمان الحال تأكيدا، والتقييد بزمان الماضي والاستقبال محتاج إلى التجريد، وكلاهما خلاف الأصل.",
     "en": "For if it were for negating the present, restricting it to present time would be emphasis, and restricting it to past or future time would require divesting [it of its proper sense], and both are contrary to the default."},
    {"type": "pair",
     "ar": "قال الأندلسي: ليس بين القولين تناقض؛ لأن خبر ليس إن لم يقيد بزمان يحمل على الحال كما يحمل الإيجاب عليه في نحو: زيد قائم، وإذا قيد بزمان من الأزمنة، فهو على ما قيد به،",
     "en": "Al-Andalusī said: there is no contradiction between the two views, because the predicate of “laysa”, if it is not restricted to a time, is taken as present, just as the affirmative is taken so in such as “Zaydun qāʾimun”; and when it is restricted to one of the times, it follows what it is restricted to."},
    {"type": "pair",
     "ar": "كذا في الرضي هذا إذا كان الاختلاف بينهم في الاستعمال، كما يشير إليه قوله: يحمل،",
     "en": "So it is in al-Raḍī. This holds if the disagreement among them concerns usage, as his word “is taken” indicates;"},
    {"type": "pair",
     "ar": "لكن الظاهر أن الاختلاف المذكور في الوضع، فالتناقض بين المذهبين باق،",
     "en": "but the apparent [reading] is that the disagreement mentioned concerns the original coinage (waḍʿ), so the contradiction between the two views remains;"},
    {"type": "pair",
     "ar": "ودليل المذهب الثاني راجح؛ لأن الاستعمال بتقييده بالأزمنة الثلاثة يدل على أنه موضوع للقدر المشترك لئلا يلزم القول بالاشتراك أو بالحقيقة والمجاز، والأصل ينفيهما.",
     "en": "and the proof of the second view is preferable, because its usage with restriction to the three times indicates that it is coined for the common measure, lest one be compelled to hold [verbal] homonymy (ishtirāk) or literal and figurative use, both of which the default rules out."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "فإن «يأتيهم» دليل على أن \"ليس\" للاستقبال.",
     "en": "For “yaʾtīhim” (it comes to them) is evidence that “laysa” is for the future."},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "سورة هود: ٨.",
     "en": "Qurʾān, Sūrat Hūd 11:8."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "إما تأكيد للمضاف أو للمضاف إليه، لكن جعله تأكيدا للمضاف أولى؛ لأنه الشائع",
     "en": "It is emphasis either of the first term of the genitive construction or of the second; but making it emphasis of the first term is preferable, because that is the common usage,"},
    {"type": "pair",
     "ar": "ولعدم الاعتداد بقول من قال: إنه لا يجوز تقديم خبر ما دام لكونه مخالفا للنص، والقياس والإجماع على ما في شرح التسهيل.",
     "en": "and because no account is taken of the view of whoever said that the predicate of “mā dāma” may not be placed first, since it contradicts the explicit text, analogy and consensus, according to what is in Sharḥ al-Tashīl."},
]
