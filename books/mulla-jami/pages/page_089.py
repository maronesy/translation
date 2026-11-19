# -*- coding: utf-8 -*-
"""Mulla Jami — al-Fawāʾid al-Ḍiyāʾiyya. Source PDF page 89 (printed ٨٨).

The remaining grounds' secondariness, and the ruling that the diptote may be
made declinable (ṣarf) for poetic necessity.
"""

PAGE_NUMBER = 89
PRINTED_PAGE = "٨٨"   # Arabic-Indic, as printed

BLOCKS = [
    # ---------------- The base text (matn) ----------------
    {"type": "matn",
     "ar": "والجمع فرع الواحد.",
     "en": "and the plural is secondary to the singular;"},
    {"type": "matn",
     "ar": "والتركيب فرع الإفراد.",
     "en": "and compounding is secondary to being a single [uncompounded] word (ifrād);"},
    {"type": "matn",
     "ar": "والألف والنون الزائدتان فرع ما زيدتا عليه[[١]]. ووزن الفعل فرع وزن الاسم؛ لأن أصل كل نوع[[٢]] ألا يكون فيه الوزن المختص بنوع آخر، فإذا وجد فيه هذا الوزن كان فرعا لوزنه الأصلي.",
     "en": "and the adjunct alif and nūn are secondary to that to which they are added; and the pattern of the verb is secondary to the pattern of the noun — because the primary state of each kind [of word] is that it should not carry the pattern proper to another kind; so when this [verbal] pattern is found in it, it becomes secondary to its own original pattern."},
    {"type": "matn",
     "ar": "(ويجوز) أي: لا يمتنع[[٣]] سواء كان ضروريا أو غير ضروري (صرفه)[[٤]] أي: جعله في حكم المنصرف بإدخال الكسر والتنوين فيه، لا جعله منصرفا حقيقة،",
     "en": "“(Wa-yajūzu)” — that is: it is not prevented, whether [the case] be one of necessity or not — “(ṣarfuhu)” its being made declinable — that is: placing it under the ruling of the declinable by introducing the kasra and tanwīn into it, not making it genuinely declinable;"},
    {"type": "matn",
     "ar": "فإن غير المنصرف عند المصنف: ما فيه علتان أو واحدة تقوم مقامهما، وبإدخال الكسر والتنوين لا يلزم خلو الاسم عنهما[[٥]].",
     "en": "for the non-declinable, in the author’s usage, is that in which there are two causes, or one standing in place of the two; and by introducing the kasra and the tanwīn it does not follow that the noun is void of them [the two causes]."},
    {"type": "matn",
     "ar": "وقيل: المراد بالصرف[[٦]] معناه اللغوي[[٧]] لا الاصطلاحي.",
     "en": "It is [also] said: what is meant by “ṣarf” is its linguistic sense, not the technical one."},
    {"type": "matn",
     "ar": "والضمير في «صرفه» راجع إلى «حكمه».",
     "en": "The pronoun in “ṣarfihi” refers back to “ḥukmihi” (its ruling)."},

    {"type": "rule"},

    # ---------------- Footnote 1 ----------------
    {"type": "note", "num": "١"},
    {"type": "pair",
     "ar": "منهم من قال: إن منعهما للصرف لمضارعتهما لألفي التأنيث الممدودة في انتفاء التاء، وكونهما زيدتا معا وحذفتا معا، وكون أولى الحرفين في كل مدة والثانية حرفا شبيها بحرف العلة.",
     "en": "Some of them said: their [the alif and nūn’s] preventing declension is by reason of their resemblance to the extended alif of feminization (alif al-taʾnīth al-mamdūda) — in the absence of the tāʾ, in that both are added together and elided together, and in that the first of the two letters is in every case a [long] prolongation and the second a letter resembling a weak letter (ḥarf al-ʿilla)."},
    {"type": "pair",
     "ar": "ولا يخفى أنه لا بد حينئذ من إثبات الفرعية بين المشبه والمشبه به.",
     "en": "And it is not hidden that, in that case, one must [still] establish the secondariness as between the likened and that to which it is likened."},

    # ---------------- Footnote 2 ----------------
    {"type": "note", "num": "٢"},
    {"type": "pair",
     "ar": "يفيد فرعية قسم إلى القسم الآخر الذي في أوله إحدى الزوائد الأربع.",
     "en": "It indicates the secondariness of one division relative to the other division — that at the beginning of which stands one of the four augmentative [prefix] letters [of the imperfect]."},

    # ---------------- Footnote 3 ----------------
    {"type": "note", "num": "٣"},
    {"type": "pair",
     "ar": "الجواز قد يراد به الإمكان الخاص، وهو سلب الضرورة عن الطرفين. وقد يراد به الإمكان العام، وهو سلب الضرورة عن الجانب المقابل.",
     "en": "By “permissibility” (jawāz) may be intended particular possibility (al-imkān al-khāṣṣ), which is the negation of necessity from both sides. And it may intend general possibility (al-imkān al-ʿāmm), which is the negation of necessity from the opposite side alone."},
    {"type": "pair",
     "ar": "ولا يجوز إرادة المعنى الأول لوجوب الصرف في الضرورة، بل يراد به المعنى الثاني، ويقيد بجانب الوجود، فلذا فسره بقوله: لا يمتنع.",
     "en": "The first sense cannot be intended, because declension is obligatory in the case of [poetic] necessity; rather the second sense is intended, restricted to the side of realization (al-wujūd) — which is why he glossed it by his words “it is not prevented.”"},

    # ---------------- Footnote 4 ----------------
    {"type": "note", "num": "٤"},
    {"type": "pair",
     "ar": "لا يجوز عكسه، وذلك لأن الضرورة ترد الأشياء إلى أصولها، ولا تخرج الأشياء عن أصولها.",
     "en": "Its reverse is not permissible; that is because [poetic] necessity returns things to their origins, and does not take things out of their origins."},
    {"type": "pair",
     "ar": "ولهذا جاز قصر الممدود في الشعر دون مد المقصور إلا نادرا. وجوز الكوفيون وبعض البصريين العكس للضرورة بشرط العلمية.",
     "en": "For this reason the shortening of a [normally] extended [alif] is permitted in poetry, but not the extending of a [normally] shortened one, except rarely. The Kūfans and some of the Basrans permitted the reverse for [poetic] necessity, on condition of proper-name status (ʿalamiyya)."},

    # ---------------- Footnote 5 ----------------
    {"type": "note", "num": "٥"},
    {"type": "pair",
     "ar": "فيه أن غير المنصرف ما فيه علتان مؤثرتان، فيجوز أن تخرجا من التأثير بالضرورة أو باعتبار التناسب، فلا حاجة إلى ضرورة الصرف عن ظاهره.",
     "en": "In this [there is a point]: that the non-declinable is one in which there are two effective causes, so it is possible that the two [causes] withdraw from [having] effect, by [poetic] necessity or by the consideration of correspondence (tanāsub); hence there is no need [to construe] the necessity of declension against its apparent [sense]."},

    # ---------------- Footnote 6 ----------------
    {"type": "note", "num": "٦"},
    {"type": "pair",
     "ar": "قائله: الشارح الهندي. وإنما أتى بصيغة التمريض إشارة إلى ضعفه؛ لأن المناسب بالمقام هو الأول.",
     "en": "Its author is the Indian commentator (al-Shāriḥ al-Hindī). He used the weakening construction [“it is said”] only to indicate its weakness, because what suits the context is the first [view]."},
    {"type": "pair",
     "ar": "مع أن الثاني معنى مجاز بالنسبة إلى اصطلاح النحاة، وإن كان حقيقة بالنسبة إلى اللغة، ومعناه اللغوي التغيير، ومعناه الاصطلاحي الخلو عن العلتين.",
     "en": "Moreover the second is a figurative sense in relation to the technical usage of the grammarians, even though it is literal in relation to the [ordinary] language; its linguistic sense is “alteration” (taghyīr), and its technical sense is “being void of the two causes.”"},

    # ---------------- Footnote 7 ----------------
    {"type": "note", "num": "٧"},
    {"type": "pair",
     "ar": "الظاهر من الصرف معناه الاصطلاحي. والظاهر من ضمير «صرفه» رجوعه إلى غير المنصرف بحكم قوله: وحكمه.",
     "en": "The apparent [sense] of “ṣarf” is its technical meaning. And the apparent [referent] of the pronoun in “ṣarfihi” is its referring back to the non-declinable [noun], by virtue of his words “and its ruling.”"},
    {"type": "pair",
     "ar": "والحاجة تندفع بترك الظاهر الأول؛ فلا وجه لترك الظاهر الثاني، فافهم.",
     "en": "The need is met by abandoning the first apparent [reading]; so there is no ground for abandoning the second apparent [reading] — so understand."},
]
